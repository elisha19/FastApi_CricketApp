from sqlalchemy.orm import Session
from . import venue_model as models, venue_schema as schemas


def get_venue_by_id(db: Session, venue_id: int):
    return db.query(models.Venue).filter(models.Venue.id == venue_id).first()


def get_venues(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Venue).offset(skip).limit(limit).all()


def create_venue(db: Session, venue: schemas.CreateVenue):
    new_venue = models.Venue(venue_name=venue.venue_name,
                             venue_location=venue.venue_location)
    db.add(new_venue)
    db.commit()
    db.refresh(new_venue)
    return new_venue


def update_venue_by_id(db: Session, venue_id, venue):
    db_venue = get_venue_by_id(db, venue_id=venue_id)

    db_venue.venue_name = venue.venue_name
    db_venue.venue_location = venue.venue_location

    db.commit()
    db.refresh(db_venue)
    return db_venue


def delete_venue_by_id(db: Session, venue_id: int):
    deleted_venue = db.query(models.Venue).filter(models.Venue.id == venue_id).first()
    db.delete(deleted_venue)
    db.commit()
    return deleted_venue
