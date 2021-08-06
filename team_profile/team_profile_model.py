from sqlalchemy import Integer, ForeignKey, Column
from database import Base

class TeamProfile(Base):
    __tablename__ = "TeamProfile"

    id = Column(Integer, primary_key=True)
    total_wins = Column(Integer, nullable=True)
    total_loses = Column(Integer, nullable=True)
    no_of_matches = Column(Integer, nullable=True)
    rank = Column(Integer, nullable=True)
    team_id = Column(Integer, ForeignKey('Team.id'))
