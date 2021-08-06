from pydantic import BaseModel


class BaseTeamProfile(BaseModel):
    total_wins: int
    total_loses: int
    no_of_matches: int
    rank: int
    team_id: int

    class Config:
        orm_mode = True

class CreateTeamProfile(BaseTeamProfile):
    pass


class UpdateTeamProfile(BaseTeamProfile):
    pass


class TeamProfile(BaseTeamProfile):
    id: int


