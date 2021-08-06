from sqlalchemy.orm import Session
from database import engine
from match_result import match_result_schema as schemas, match_result_model as models

models.Base.metadata.create_all(bind=engine)


def get_match_result_by_id(db: Session, match_result_id: int):
    return db.query(models.MatchResult).filter(models.MatchResult.id == match_result_id).first()


def get_match_results(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MatchResult).offset(skip).limit(limit).all()


def create_match_result(db: Session, match_result: schemas.CreateMatchResult):
    new_match_result = models.MatchResult(match_result=match_result.match_result)
    db.add(new_match_result)
    db.commit()
    db.refresh(new_match_result)
    return new_match_result

def update_match_result_by_id(db: Session, match_result_id, match_result):
    db_match_result = get_match_result_by_id(db, match_result_id=match_result_id)
    db_match_result.match_result = match_result.match_result
    db.commit()
    db.refresh(db_match_result)
    return db_match_result


def delete_match_result_by_id(db: Session, match_result_id: int):
    deleted_match_result = db.query(models.MatchResult).filter(models.MatchResult.id == match_result_id).first()
    db.delete(deleted_match_result)
    db.commit()
    return deleted_match_result
