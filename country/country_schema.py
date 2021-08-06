from pydantic import BaseModel


class BaseCountry(BaseModel):
    # team_name: Optional[str] = None

    country_name: str

    class Config:
        orm_mode = True


class CreateCountry(BaseCountry):
    pass


class UpdateCountry(BaseCountry):
    pass


class Country(BaseCountry):
    id: int

