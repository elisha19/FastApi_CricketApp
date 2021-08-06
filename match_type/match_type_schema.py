from pydantic import BaseModel


class BaseMatchType(BaseModel):

    match_type: str

    class Config:
        orm_mode = True


class CreateMatchType(BaseMatchType):
    pass


class UpdateMatchType(BaseMatchType):
    pass


class MatchType(BaseMatchType):
    id: int

    class Config:
        orm_mode = True
