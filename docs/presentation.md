# Project Presentation: Internship Recommendation System

## Slide 1: Title Slide
- **Title**: Machine Learning-Based Internship Recommendation System
- **Subtitle**: Using TF-IDF and Cosine Similarity
- **Presenter**: [Your Name]
- **Date**: [Current Date]

## Slide 2: Problem Statement
- **Issue**: Students struggle to find relevant internships matching their skills, location, and interests.
- **Solution**: AI-powered system that recommends top internships based on profile matching.
- **Impact**: Improves job placement and reduces search time.

## Slide 3: Objectives
- Build a recommendation model using text similarity.
- Integrate with a user-friendly web interface.
- Use real-world data from Internshala.
- Ensure scalability and accuracy.

## Slide 4: System Architecture
- **Frontend**: HTML/CSS/JS form and card display.
- **Backend**: Flask API for ML processing.
- **Model**: TF-IDF + Cosine Similarity.
- **Data**: CSV datasets for internships and students.

## Slide 5: Data Sources
- **Internships**: Scraped from Internshala (6,694 entries).
- **Students**: Sample profiles (5 entries).
- **Features**: Title, Company, Location, Skills, Education.

## Slide 6: Machine Learning Process
1. **Preprocessing**: Combine text fields.
2. **Vectorization**: TF-IDF for numerical representation.
3. **Similarity**: Cosine similarity for matching.
4. **Ranking**: Top 5 based on scores and filters.

## Slide 7: Key Features
- Dynamic form input.
- Clickable cards linking to Internshala.
- Real-time recommendations.
- CSV output for easy analysis.

## Slide 8: Demonstration
- Show the UI: Form filling and recommendation display.
- Example: Student in Bangalore with Tech skills → Machine Learning internships.

## Slide 9: Results and Analysis
- **Accuracy**: High similarity scores for relevant matches.
- **Performance**: Efficient with large datasets.
- **Limitations**: Text-based; no deep learning yet.

## Slide 10: SDG Mapping (See docs/sdg_mapping.md)

## Slide 11: Future Work
- Integrate BERT for semantic matching.
- Add user feedback loop.
- Expand to other job platforms.

## Slide 12: Q&A
- Thank you for your attention!
- Open for questions.
