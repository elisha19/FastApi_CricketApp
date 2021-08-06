from pydantic import BaseModel


class BaseTeam(BaseModel):
    # team_name: Optional[str] = None

    team_name: str
    country_id: int

    class Config:
        orm_mode = True


class CreateTeam(BaseTeam):
    pass


class UpdateTeam(BaseTeam):
    pass


class Team(BaseTeam):
    id: int

    class Config:
        orm_mode = True
