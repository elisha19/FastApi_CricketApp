from pydantic import BaseModel
from datetime import date


class BasePlayer(BaseModel):
    name: str
    age: int
    dob: date
    retirement_date: date
    player_role_id: int
    team_id: int

    class Config:
        orm_mode = True

class CreatePlayer(BasePlayer):
    pass


class UpdatePlayer(BasePlayer):
    pass


class Player(BasePlayer):
    id: int


