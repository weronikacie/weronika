from sqlalchemy import Column, Integer, String
from db_base import Base


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    movie_id = Column(Integer)
    tag = Column(String)
    timestamp = Column(Integer)
