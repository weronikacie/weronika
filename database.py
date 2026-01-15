from models.tag import Tag
from models.rating import Rating
from models.link import Link
from models.movie import Movie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_base import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)
