from sqlalchemy.orm import Session
from database import engine
from match import match_schema as schemas, match_model as models

models.Base.metadata.create_all(bind=engine)


def get_match_by_id(db: Session, match_id: int):
    return db.query(models.Match).filter(models.Match.id == match_id).first()


def get_matches(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Match).offset(skip).limit(limit).all()


def create_match(db: Session, match: schemas.CreateMatch):
    new_match = models.Match(match_date=match.match_date,
                             venue_id=match.venue_id,
                             tournament_id=match.tournament_id)
    db.add(new_match)
    db.commit()
    db.refresh(new_match)
    return new_match

def update_match_by_id(db: Session, match_id, match):
    db_match = get_match_by_id(db, match_id=match_id)
    db_match.match_date = match.match_date
    db_match.venue_id = match.venue_id
    db_match.tournament_id = match.tournament_id
    db.commit()
    db.refresh(db_match)
    return db_match


def delete_match_by_id(db: Session, match_id: int):
    deleted_match = db.query(models.Match).filter(models.Match.id == match_id).first()
    db.delete(deleted_match)
    db.commit()
    return deleted_match
