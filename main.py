from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import difflib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

movies_data = None
similarity = None
titles = None

class MovieRequest(BaseModel):
    movie: str

@app.on_event("startup")
def load_model():
    global movies_data, similarity, titles

    movies_data = pd.read_csv("movies.csv")

    features = ["genres", "keywords", "tagline", "cast", "director"]
    for f in features:
        movies_data[f] = movies_data[f].fillna("")

    combined = (
        movies_data["genres"] + " " +
        movies_data["keywords"] + " " +
        movies_data["tagline"] + " " +
        movies_data["cast"] + " " +
        movies_data["director"]
    )

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(combined)
    similarity = cosine_similarity(vectors)

    titles = movies_data["title"].tolist()

@app.get("/")
def root():
    return {"status": "API running"}

@app.post("/recommendation")
def recommend(request: MovieRequest):
    movie_name = request.movie

    matches = difflib.get_close_matches(movie_name, titles, n=1)
    if not matches:
        raise HTTPException(status_code=404, detail="Movie not found")

    close_match = matches[0]
    idx = movies_data[movies_data["title"] == close_match].index[0]

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:11]

    recommendations = [
        movies_data.iloc[i[0]]["title"] for i in scores
    ]

    return {
        "matched_movie": close_match,
        "recommendations": recommendations
    }
