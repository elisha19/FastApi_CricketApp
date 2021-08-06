
from pydantic import BaseModel


class BaseMatchResult(BaseModel):

    match_result: str

    class Config:
        orm_mode = True


class CreateMatchResult(BaseMatchResult):
    pass


class UpdateMatchResult(BaseMatchResult):
    pass


class MatchResult(BaseMatchResult):
    id: int


