from sqlalchemy import Column, Integer, String
from db_base import Base


class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    genres = Column(String)
