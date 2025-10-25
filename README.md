# Internship Recommendation System

This project implements a machine learning model to recommend the top 3-5 internships to students based on their skills, education level, preferred location, and sector of interest. The model uses TF-IDF vectorization and cosine similarity for text matching.

## Features

- **Dynamic Student Input**: Form-based interface where students enter their details.
- **Clickable Recommendations**: Click on any recommendation card or the "View Full Details" button to open the full internship page on Internshala in a new tab.
- **TF-IDF Vectorization**: Converts student profiles and internship descriptions into numerical vectors.
- **Cosine Similarity**: Measures similarity between student and internship vectors.
- **Filtering and Ranking**: Prioritizes location matches, then ranks by similarity scores.
- **API Integration**: Flask API to serve recommendations.

## Data

- **whole_Internshala_scraped2.csv**: Real scraped dataset from Internshala with 6694 internship listings, including fields like Title, Company Name, Location, Stipend, Duration, Links, etc.
- **students.csv**: Sample student profiles with skills, education, location, and sector preferences.
- **recommendations.csv**: Generated recommendations for each student based on the model.

## Documentation

For detailed project information, check the `docs/` folder:
- **architecture.md**: System architecture and components.
- **data_dictionary.md**: Description of datasets and fields.
- **presentation.md**: Project presentation outline.
- **sdg_mapping.md**: Mapping to Sustainable Development Goals (SDGs).

## Installation

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the recommendation script to generate recommendations in CSV:
   ```
   python internship_recommender.py
   ```

3. Start the Flask API:
   ```
   python app.py
   ```
   The API will run on `http://localhost:5000`.

4. Serve the frontend:
   ```
   python -m http.server 8000
   ```
   Access the UI at `http://localhost:8000/index.html`.

## User Interface

- Open `index.html` in a browser.
- Fill out the form with your details:
  - Name (optional)
  - Education Level (dropdown)
  - Preferred Location
  - Sector of Interest
  - Skills (comma-separated)
- Click "Get Recommendations" to receive personalized suggestions.

## API Usage

Send a POST request to `/recommend` with JSON payload:
```json
{
  "name": "John Doe",
  "education_level": "Undergraduate",
  "preferred_location": "Bangalore",
  "sector_of_interest": "Technology",
  "skills": "Python, Java, Machine Learning"
}
```

Response:
```json
{
  "recommendations": [
    {
      "internship_id": 123,
      "title": "Flutter Development",
      "company": "Kartavya Technology",
      "location": "Work From Home",
      "stipend": "₹ 10,000 /month",
      "duration": "Starts immediatelyImmediately",
      "link": "https://internshala.com/internship/detail/...",
      "similarity_score": 0.227
    },
    ...
  ]
}
```

## Model Details

- Combines text fields (Title, Company Name, Location) for TF-IDF.
- Filters by location first, then ranks by cosine similarity scores.
- Ranks top 3-5 based on similarity scores.
- For new student input, vectorizes on-the-fly and computes similarity with all internships.

## Testing

Fill out the form with sample data:
- Education: Undergraduate
- Location: Bangalore
- Sector: Technology
- Skills: Python, Java, Machine Learning

The model will return relevant internships from the 6694-row dataset.

## Analysis Results

- The model processes 6694 internships in real-time for each query.
- Recommendations are based on text similarity and location matching.
- Example: A student with Tech skills in Bangalore gets high-similarity matches from relevant internships.

## Future Improvements

- Add more diverse student data.
- Incorporate additional features like stipend range or duration.
- Use advanced models like BERT for semantic matching.
