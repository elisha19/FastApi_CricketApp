from sqlalchemy.orm import Session
from database import engine
from match_type import match_type_schema as schemas, match_type_model as models

models.Base.metadata.create_all(bind=engine)


def get_match_type_by_id(db: Session, match_type_id: int):
    return db.query(models.MatchType).filter(models.MatchType.id == match_type_id).first()


def get_match_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MatchType).offset(skip).limit(limit).all()


def create_match_type(db: Session, match_type: schemas.CreateMatchType):
    new_match_type = models.MatchType(match_type=match_type.match_type)
    db.add(new_match_type)
    db.commit()
    db.refresh(new_match_type)
    return new_match_type

def update_match_type_by_id(db: Session, match_type_id, match_type):
    db_match_type = get_match_type_by_id(db, match_type_id=match_type_id)
    db_match_type.match_type = match_type.match_type
    db.commit()
    db.refresh(db_match_type)
    return db_match_type


def delete_match_type_by_id(db: Session, match_type_id: int):
    deleted_match_type = db.query(models.MatchType).filter(models.MatchType.id == match_type_id).first()
    db.delete(deleted_match_type)
    db.commit()
    return deleted_match_type
