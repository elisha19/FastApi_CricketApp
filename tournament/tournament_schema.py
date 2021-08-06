from pydantic import BaseModel
from datetime import date


class BaseTournament(BaseModel):
    name: str
    first_place_team_id: int
    second_place_team_id: int
    third_place_team_id: int
    start_date: date
    end_date: date
    total_points: int
    team_id: int

    class Config:
        orm_mode = True

class CreateTournament(BaseTournament):
    pass

class UpdateTournament(BaseTournament):
    pass

class Tournament(BaseTournament):
    id: int


