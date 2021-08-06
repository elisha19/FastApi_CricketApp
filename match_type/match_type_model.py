from sqlalchemy import Column, Integer, String
from database import Base


class MatchType(Base):
    __tablename__ = "MatchType"

    id = Column(Integer, primary_key=True)
    match_type = Column(String, nullable=True)
