# System Architecture

## Overview
The Internship Recommendation System is a machine learning-based application that matches students with internships using text similarity techniques. The system is built with Python for the backend, HTML/CSS/JS for the frontend, and leverages TF-IDF and cosine similarity for recommendations.

## Architecture Diagram
```
User Input (Form) --> Frontend (HTML/CSS/JS) --> API (Flask) --> ML Model (TF-IDF + Cosine Similarity) --> Database (CSV Files) --> Recommendations (CSV/JSON) --> UI Display
```

## Components

### 1. Frontend (User Interface)
- **Technology**: HTML, CSS, JavaScript
- **Purpose**: Interactive form for student input and display of recommendations.
- **Features**: Form validation, loading states, clickable cards for links.
- **Files**: index.html, styles.css, script.js

### 2. Backend (API)
- **Technology**: Flask (Python)
- **Purpose**: Handles API requests, processes ML model, and returns recommendations.
- **Features**: CORS support, dynamic profile processing, error handling.
- **Files**: app.py

### 3. Machine Learning Model
- **Technology**: Scikit-learn (Python)
- **Purpose**: Vectorizes text and computes similarities.
- **Algorithms**:
  - TF-IDF Vectorization: Converts text to numerical vectors.
  - Cosine Similarity: Measures similarity between profiles and internships.
- **Files**: internship_recommender.py

### 4. Data Storage
- **Technology**: CSV Files (Pandas)
- **Purpose**: Stores internship data and student profiles.
- **Files**: whole_Internshala_scraped2.csv (internships), students.csv (profiles), recommendations.csv (output)

## Data Flow
1. User submits form with profile details.
2. Frontend sends POST request to Flask API.
3. API processes input, computes similarities using ML model.
4. Returns top recommendations.
5. Frontend displays cards with links to Internshala.

## Deployment
- **Frontend**: Static server (python -m http.server 8000).
- **Backend**: Flask server (localhost:5000).
- **Scalability**: Handles real-time queries with precomputed vectors for efficiency.
