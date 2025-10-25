import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

# Load data from CSV
internships_df = pd.read_csv('whole_Internshala_scraped2.csv')
students_df = pd.read_csv('students.csv')

# Create combined text for TF-IDF
def create_combined_text(row, fields):
    return ' '.join([str(row[field]) for field in fields])

# Fields for internships
intern_fields = ['Title', 'Company Name', 'Location']
internships_df['combined_text'] = internships_df.apply(lambda row: create_combined_text(row, intern_fields), axis=1)

# Fields for students
student_fields = ['skills', 'education_level', 'preferred_location', 'sector_of_interest']
students_df['combined_text'] = students_df.apply(lambda row: create_combined_text(row, student_fields), axis=1)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(internships_df['combined_text'].tolist() + students_df['combined_text'].tolist())

# Separate matrices
intern_tfidf = tfidf_matrix[:len(internships_df)]
student_tfidf = tfidf_matrix[len(internships_df):]

# Compute cosine similarity
similarity_matrix = cosine_similarity(student_tfidf, intern_tfidf)

# Function to get top recommendations
def get_top_recommendations(student_profile, top_n=5):
    # Create combined text for the student
    student_combined = create_combined_text(student_profile, ['skills', 'education_level', 'preferred_location', 'sector_of_interest'])
    student_tfidf = vectorizer.transform([student_combined])
    
    # Compute similarity
    similarity_scores = cosine_similarity(student_tfidf, intern_tfidf).flatten()
    
    # Get top indices
    top_indices = similarity_scores.argsort()[-top_n*2:][::-1]  # Get more to filter
    
    recommendations = []
    filters = student_profile.get('filters', {})
    min_stipend = filters.get('min_stipend', '')
    max_stipend = filters.get('max_stipend', '')
    duration_pref = filters.get('duration', '')
    work_type_pref = filters.get('work_type', '')
    
    for idx in top_indices:
        intern = internships_df.iloc[idx]
        
        # Parse stipend
        stipend_str = intern['Stipend']
        stipend_val = 0
        if '₹' in stipend_str:
            # Extract numbers, handle commas
            numbers = [int(num.replace(',', '')) for num in re.findall(r'\d{1,3}(?:,\d{3})*', stipend_str)]
            if numbers:
                stipend_val = numbers[0]  # Take the first number
        
        # Check filters
        stipend_match = True
        if min_stipend and stipend_val < int(min_stipend):
            stipend_match = False
        if max_stipend and stipend_val > int(max_stipend):
            stipend_match = False
        
        duration_match = True
        if duration_pref:
            duration_str = intern['Duration'].lower()
            # Map duration preferences to keywords
            duration_keywords = {
                '1-2 months': ['month', '1', '2'],
                '3-6 months': ['month', '3', '6'],
                '6+ months': ['month', '6', '12']
            }
            if duration_pref in duration_keywords:
                keywords = duration_keywords[duration_pref]
                if not any(kw in duration_str for kw in keywords):
                    duration_match = False
        
        work_type_match = True
        if work_type_pref:
            location_str = intern['Location'].lower()
            if work_type_pref.lower() not in location_str:
                work_type_match = False
        
        # Filter by location if specified
        location_match = True
        if student_profile.get('preferred_location') and student_profile['preferred_location'].lower() not in intern['Location'].lower():
            location_match = False
        
        if stipend_match and duration_match and work_type_match and location_match:
            recommendations.append({
                'internship_id': int(intern['Unnamed: 0']),
                'title': intern['Title'],
                'company': intern['Company Name'],
                'location': intern['Location'],
                'stipend': intern['Stipend'],
                'duration': intern['Duration'],
                'link': intern['Links'],
                'similarity_score': float(similarity_scores[idx])
            })
    
    if len(recommendations) < top_n:
        # Fallback: Get top without filters
        for idx in top_indices:
            intern = internships_df.iloc[idx]
            if not any(r['internship_id'] == int(intern['Unnamed: 0']) for r in recommendations):
                recommendations.append({
                    'internship_id': int(intern['Unnamed: 0']),
                    'title': intern['Title'],
                    'company': intern['Company Name'],
                    'location': intern['Location'],
                    'stipend': intern['Stipend'],
                    'duration': intern['Duration'],
                    'link': intern['Links'],
                    'similarity_score': float(similarity_scores[idx])
                })
    
    return recommendations[:top_n]

# Example: Get recommendations for all students
results = {}
for _, student in students_df.iterrows():
    student_profile = {
        'education_level': student['education_level'],
        'preferred_location': student['preferred_location'],
        'sector_of_interest': student['sector_of_interest'],
        'skills': student['skills']
    }
    results[int(student['id'])] = get_top_recommendations(student_profile, top_n=5)

# Save results to CSV
rows = []
for student_id, recs in results.items():
    for rec in recs:
        rows.append({
            'student_id': student_id,
            'internship_id': rec['internship_id'],
            'title': rec['title'],
            'company': rec['company'],
            'location': rec['location'],
            'stipend': rec['stipend'],
            'duration': rec['duration'],
            'link': rec['link'],
            'similarity_score': rec['similarity_score']
        })

final_df = pd.DataFrame(rows)
final_df.to_csv('recommendations.csv', index=False)

print("Recommendations saved to recommendations.csv")
