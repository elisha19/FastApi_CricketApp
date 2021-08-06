from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from database import Base


class Match(Base):
    __tablename__ = "Match"

    id = Column(Integer, primary_key=True)
    match_date = Column(DateTime, nullable=True)
    venue_id = Column(Integer)
    tournament_id = Column(Integer, ForeignKey('Tournament.id'))
    match_summary = relationship("MatchSummary")
