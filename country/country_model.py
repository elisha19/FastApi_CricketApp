from sqlalchemy import Column, Integer, String
from database import Base

class Country(Base):
    __tablename__ = "Country"

    id = Column(Integer, primary_key=True)
    country_name = Column(String, nullable=True)
