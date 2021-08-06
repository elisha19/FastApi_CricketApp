from sqlalchemy import Column, Integer, ForeignKey
from database import Base


class PlayerBatProfile(Base):
    __tablename__ = "PlayerBatProfile"

    id = Column(Integer, primary_key=True)
    matches = Column(Integer, nullable=True)
    innings = Column(Integer, nullable=True)
    no_of_not_outs = Column(Integer, nullable=True)
    runs = Column(Integer, nullable=True)
    highest_score = Column(Integer, nullable=True)
    average = Column(Integer, nullable=True)
    no_of_balls_faced = Column(Integer, nullable=True)
    strike_rate = Column(Integer, nullable=True)
    half_centuries = Column(Integer, nullable=True)
    full_centuries = Column(Integer, nullable=True)
    boundaries = Column(Integer, nullable=True)
    sixes = Column(Integer, nullable=True)
    player_id = Column(Integer, ForeignKey('Player.id'))
