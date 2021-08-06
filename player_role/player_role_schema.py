from pydantic import BaseModel


class BasePlayerRole(BaseModel):

    role_name: str

    class Config:
        orm_mode = True


class CreatePlayerRole(BasePlayerRole):
    pass


class UpdatePlayerRole(BasePlayerRole):
    pass


class PlayerRole(BasePlayerRole):
    id: int


