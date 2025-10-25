# Data Dictionary

## Internships Dataset (whole_Internshala_scraped2.csv)

| Field Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| Unnamed: 0 | Integer | Index/ID of the internship | 1 |
| Title | String | Internship title/role | "Machine Learning" |
| Company Name | String | Name of the company | "Avaari" |
| Location | String | Internship location | "[['Work From Home']]" |
| Start Date | String | When the internship starts | "Immediately" |
| Duration | String | Length of the internship | "Starts immediatelyImmediately" |
| Stipend | String | Monthly payment | "₹ 15,000 /month" |
| Status | String | Posting status | "3 weeks ago" |
| Links | String | URL to the full internship page | "https://internshala.com/internship/detail/..." |

## Students Dataset (students.csv)

| Field Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| id | Integer | Student ID | 1 |
| name | String | Student's name | "Alice Johnson" |
| education_level | String | Education level | "Undergraduate" |
| preferred_location | String | Desired location | "Bangalore" |
| sector_of_interest | String | Preferred sector | "Technology" |
| skills | String | Comma-separated skills | "Python, Java, Machine Learning" |

## Recommendations Dataset (recommendations.csv)

| Field Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| student_id | Integer | ID of the student | 1 |
| internship_id | Integer | ID of the recommended internship | 6248 |
| title | String | Internship title | "JAVA Application Development And Machine Learning" |
| company | String | Company name | "NatWest Group" |
| location | String | Internship location | "[['Gurgaon']]" |
| stipend | String | Stipend amount | "₹ 45,000 /month" |
| duration | String | Internship duration | "Starts immediatelyImmediately" |
| link | String | Link to full details | "https://internshala.com/internship/detail/..." |
| similarity_score | Float | Cosine similarity score | 0.43447572260253564 |

## Notes
- All datasets are in CSV format for easy analysis.
- Similarity scores range from 0.0 (no match) to 1.0 (perfect match).
- Location fields may include lists (e.g., [['Work From Home']]), indicating multiple or remote options.
