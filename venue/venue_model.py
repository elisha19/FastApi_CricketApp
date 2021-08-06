from sqlalchemy import Integer, String, Column
from database import Base

class Venue(Base):
    __tablename__ = "Venue"

    id = Column(Integer, primary_key=True)
    venue_name = Column(String, nullable=True)
    venue_location = Column(String, nullable=True)
