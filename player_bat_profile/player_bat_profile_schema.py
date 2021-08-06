from pydantic import BaseModel


class BasePlayerBatProfile(BaseModel):
    matches: int
    innings: int
    no_of_not_outs: int
    runs: int
    highest_score: int
    average: int
    no_of_balls_faced: int
    strike_rate: int
    half_centuries: int
    full_centuries: int
    boundaries: int
    sixes: int
    player_id: int

    class Config:
        orm_mode = True

class CreatePlayerBatProfile(BasePlayerBatProfile):
    pass

class UpdatePlayerBatProfile(BasePlayerBatProfile):
    pass


class PlayerBatProfile(BasePlayerBatProfile):
    id: int


