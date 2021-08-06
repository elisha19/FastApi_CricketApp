from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

from database import Base


class Team(Base):
    __tablename__ = "Team"

    id = Column(Integer, primary_key=True)
    team_name = Column(String, nullable=True)
    country_id = Column(Integer)
    player = relationship("Player")
    team_profile = relationship("TeamProfile")