from sqlalchemy import Column, Integer, Float
from db_base import Base


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    movie_id = Column(Integer)
    rating = Column(Float)
    timestamp = Column(Integer)
