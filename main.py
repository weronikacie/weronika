import csv
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from models.movie import Movie
from models.link import Link
from models.rating import Rating
from models.tag import Tag

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/movies")
def get_movies():
    movies = []

    with open("data/movies.csv", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            movie = Movie(row[0], row[1], row[2])
            movies.append(movie.__dict__)

    return movies


@app.get("/links")
def get_links():
    links = []

    with open("data/links.csv", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            link = Link(row[0], row[1], row[2])
            links.append(link.__dict__)

    return links


@app.get("/ratings")
def get_ratings():
    ratings = []

    with open("data/ratings.csv", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            rating = Rating(row[0], row[1], row[2], row[3])
            ratings.append(rating.__dict__)

    return ratings


@app.get("/tags")
def get_tags():
    tags = []

    with open("data/tags.csv", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            tag = Tag(row[0], row[1], row[2], row[3])
            tags.append(tag.__dict__)

    return tags
