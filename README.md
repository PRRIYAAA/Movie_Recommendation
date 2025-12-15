# Movie Recommendation System

A content-based movie recommendation system built with FastAPI, scikit-learn, and pandas. This API provides personalized movie recommendations based on genres, keywords, taglines, cast, and director information using TF-IDF vectorization and cosine similarity.

## Features

- **Content-Based Filtering**: Recommends movies based on similar content features
- **FastAPI Backend**: High-performance REST API with automatic documentation
- **CORS Support**: Cross-origin resource sharing enabled for web applications
- **Fuzzy Matching**: Handles slight variations in movie title input using difflib
- **Real-time Recommendations**: Provides top 10 similar movies for any given movie

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd movie-recommendation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure the `movies.csv` file is in the project root directory.

## Usage

### Running the Application

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

### API Documentation

Visit `http://127.0.0.1:8000/docs` for interactive Swagger UI documentation.

## API Endpoints

### GET /
Returns API status information.

**Response:**
```json
{
  "status": "API running"
}
```

### POST /recommendation
Get movie recommendations based on a movie title.

**Request Body:**
```json
{
  "movie": "Movie Title"
}
```

**Response:**
```json
{
  "matched_movie": "Matched Movie Title",
  "recommendations": [
    "Recommended Movie 1",
    "Recommended Movie 2",
    ...
  ]
}
```

**Error Response:**
```json
{
  "detail": "Movie not found"
}
```

## Dataset

The system uses a movies dataset (`movies.csv`) containing the following columns:
- `index`: Movie index
- `budget`: Movie budget
- `genres`: Movie genres
- `homepage`: Movie homepage URL
- `id`: Movie ID
- `keywords`: Movie keywords
- `original_language`: Original language
- `original_title`: Original title
- `overview`: Movie overview
- `popularity`: Popularity score
- `production_companies`: Production companies
- `production_countries`: Production countries
- `release_date`: Release date
- `revenue`: Movie revenue
- `runtime`: Movie runtime
- `spoken_languages`: Spoken languages
- `status`: Movie status
- `tagline`: Movie tagline
- `title`: Movie title
- `vote_average`: Average vote
- `vote_count`: Vote count
- `cast`: Movie cast
- `crew`: Movie crew
- `director`: Movie director

## Dependencies

- **fastapi**: Web framework for building APIs
- **pydantic**: Data validation and serialization
- **uvicorn**: ASGI server for FastAPI
- **scikit-learn**: Machine learning library for TF-IDF and cosine similarity
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **python-multipart**: Multipart form data handling

## How It Works

1. **Data Loading**: On startup, the system loads the movies dataset and preprocesses the data.

2. **Feature Combination**: Combines relevant features (genres, keywords, tagline, cast, director) into a single text string for each movie.

3. **Vectorization**: Uses TF-IDF (Term Frequency-Inverse Document Frequency) to convert text features into numerical vectors.

4. **Similarity Calculation**: Computes cosine similarity between all movie vectors to determine similarity scores.

5. **Recommendation Generation**: For a given movie, finds the most similar movies based on cosine similarity scores and returns the top 10 recommendations.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.