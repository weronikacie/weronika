import csv
from sqlalchemy.orm import Session

from database import SessionLocal
from models.movie import Movie
from models.link import Link
from models.rating import Rating
from models.tag import Tag


def load_movies(db: Session):
    with open("data/movies.csv", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            movie = Movie(movie_id=int(row[0]), title=row[1], genres=row[2])
            db.add(movie)


def load_links(db: Session):
    with open("data/links.csv", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            link = Link(movie_id=int(row[0]), imdb_id=row[1], tmdb_id=row[2])
            db.add(link)


def load_ratings(db: Session):
    with open("data/ratings.csv", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            rating = Rating(
                user_id=int(row[0]),
                movie_id=int(row[1]),
                rating=float(row[2]),
                timestamp=int(row[3])
            )
            db.add(rating)


def load_tags(db: Session):
    with open("data/tags.csv", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            tag = Tag(
                user_id=int(row[0]),
                movie_id=int(row[1]),
                tag=row[2],
                timestamp=int(row[3])
            )
            db.add(tag)


def main():
    db = SessionLocal()
    load_movies(db)
    load_links(db)
    load_ratings(db)
    load_tags(db)
    db.commit()
    db.close()


if __name__ == "__main__":
    main()
