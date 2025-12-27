from sqlalchemy import Column, Integer, String
from db_base import Base

class Link(Base):
    __tablename__ = "links"

    movie_id = Column(Integer, primary_key=True)
    imdb_id = Column(String)
    tmdb_id = Column(String)
