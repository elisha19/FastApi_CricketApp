from sqlalchemy import String, Column, Integer, ForeignKey
from database import Base


class PlayerBowlProfile(Base):
    __tablename__ = "PlayerBowlProfile"

    id = Column(Integer, primary_key=True)
    matches = Column(Integer, nullable=True)
    innings = Column(Integer, nullable=True)
    no_of_deliveries = Column(Integer, nullable=True)
    runs = Column(Integer, nullable=True)
    wickets = Column(Integer, nullable=True)
    best_bowling_in_match = Column(Integer, nullable=True)
    economy = Column(String, nullable=True)
    average = Column(Integer, nullable=True)
    SR = Column(String, nullable=True)
    W5 = Column(String, nullable=True)
    W10 = Column(String, nullable=True)
    player_id = Column(Integer, ForeignKey('Player.id'))
