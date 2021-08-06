from sqlalchemy import Column, Integer, String
from database import Base


class MatchResult(Base):
    __tablename__ = "MatchResult"

    id = Column(Integer, primary_key=True)
    match_result = Column(String, nullable=True)
