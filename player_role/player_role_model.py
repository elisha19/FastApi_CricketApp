from sqlalchemy import Column, Integer, String

from database import Base

class PlayerRole(Base):
    __tablename__ = "PlayerRole"

    id = Column(Integer, primary_key=True)
    role_name = Column(String, nullable=True)
