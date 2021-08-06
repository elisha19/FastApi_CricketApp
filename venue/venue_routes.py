from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from . import venue_curd
from . import venue_schema
from dependencies import get_db

router = APIRouter()

@router.get("/venue/{venue_id}", response_model=venue_schema.BaseVenue, tags=['Venue'])
def read_venue_by_id(venue_id: int, db: Session = Depends(get_db)):
    db_venue = venue_curd.get_venue_by_id(db, venue_id=venue_id)
    if db_venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")
    return db_venue


@router.get("/venues/", response_model=List[venue_schema.BaseVenue], tags=['Venue'])
def read_venues(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    venues = venue_curd.get_venues(db, skip=skip, limit=limit)
    return venues


@router.post("/new_venue/", response_model=venue_schema.BaseVenue, tags=['Venue'])
def create_venue(venue: venue_schema.CreateVenue, db: Session = Depends(get_db)):
    db_user = venue_curd.create_venue(db, venue)
    if db_user:
        raise HTTPException(status_code=200, detail="Venue Created")
    return venue_curd.create_venue(db, venue)


@router.patch("/update_venue/{venue_id}", response_model=venue_schema.UpdateVenue, tags=['Venue'])
def update_venue(venue_id: int, venue: venue_schema.UpdateVenue, db: Session = Depends(get_db)):
    updated_venue = venue_curd.update_venue_by_id(db, venue_id, venue)
    if updated_venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")
    return updated_venue


@router.delete("/delete_venue/{venue_id}", response_model=venue_schema.BaseVenue, tags=['Venue'])
def delete_venue_by_id(venue_id: int, db: Session = Depends(get_db)):
    db_venue = venue_curd.delete_venue_by_id(db, venue_id=venue_id)
    if db_venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")
    return db_venue
