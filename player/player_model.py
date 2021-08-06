from sqlalchemy import String, Column, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Player(Base):
    __tablename__ = "Player"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    dob = Column(DateTime, nullable=True)
    retirement_date = Column(DateTime, nullable=True)
    player_role_id = Column(Integer)
    team_id = Column(Integer, ForeignKey('Team.id'))
    player_bat_profile = relationship("PlayerBatProfile")
    player_bowl_profile = relationship("PlayerBowlProfile")
