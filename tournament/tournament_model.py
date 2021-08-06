from sqlalchemy import Integer, String, DateTime,Column
from sqlalchemy.orm import relationship
from database import Base


class Tournament(Base):
    __tablename__ = "Tournament"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    first_place_team_id = Column(String, nullable=True)
    second_place_team_id = Column(String, nullable=True)
    third_place_team_id = Column(String, nullable=True)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    total_points = Column(Integer, nullable=True)
    team_id = Column(Integer)
    match = relationship("Match")
