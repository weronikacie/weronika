from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.movie import Movie
from models.link import Link
from models.rating import Rating
from models.tag import Tag

app = FastAPI()


# połączenie z bazą
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"status": "API with SQLite is running"}


@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    movies = db.query(Movie).all()
    return [
        {"movie_id": m.movie_id, "title": m.title, "genres": m.genres}
        for m in movies
    ]


@app.get("/links")
def get_links(db: Session = Depends(get_db)):
    links = db.query(Link).all()
    return [
        {"movie_id": l.movie_id, "imdb_id": l.imdb_id, "tmdb_id": l.tmdb_id}
        for l in links
    ]


@app.get("/ratings")
def get_ratings(db: Session = Depends(get_db)):
    ratings = db.query(Rating).all()
    return [
        {
            "user_id": r.user_id,
            "movie_id": r.movie_id,
            "rating": r.rating,
            "timestamp": r.timestamp
        }
        for r in ratings
    ]


@app.get("/tags")
def get_tags(db: Session = Depends(get_db)):
    tags = db.query(Tag).all()
    return [
        {
            "user_id": t.user_id,
            "movie_id": t.movie_id,
            "tag": t.tag,
            "timestamp": t.timestamp
        }
        for t in tags
    ]

