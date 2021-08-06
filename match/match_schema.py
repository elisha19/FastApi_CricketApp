from datetime import date
from pydantic import BaseModel


class BaseMatch(BaseModel):
    match_date: date
    venue_id: int
    tournament_id: int

    class Config:
        orm_mode = True


class CreateMatch(BaseMatch):
    pass


class UpdateMatch(BaseMatch):
    pass


class Match(BaseMatch):
    id: int

