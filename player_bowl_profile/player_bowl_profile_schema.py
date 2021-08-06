from pydantic import BaseModel


class BasePlayerBowlProfile(BaseModel):
    matches: int
    innings: int
    no_of_deliveries: int
    runs: int
    wickets: int
    best_bowling_in_match: int
    economy: str
    average: str
    SR: str
    W5: str
    W10: str
    player_id: int

    class Config:
        orm_mode = True

class CreatePlayerBowlProfile(BasePlayerBowlProfile):
    pass


class UpdatePlayerBowlProfile(BasePlayerBowlProfile):
    pass


class PlayerBowlProfile(BasePlayerBowlProfile):
    id: int


