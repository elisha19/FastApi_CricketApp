from pydantic import BaseModel


class BaseVenue(BaseModel):
    venue_name: str
    venue_location: str

    class Config:
        orm_mode = True

class CreateVenue(BaseVenue):
    pass

class UpdateVenue(BaseVenue):
    pass

class Venue(BaseVenue):
    id: int


