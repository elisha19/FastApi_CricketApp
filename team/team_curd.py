from sqlalchemy.orm import Session
from database import engine
from team import team_schema as schemas, team_model as models

models.Base.metadata.create_all(bind=engine)


def get_team_by_id(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()


def get_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Team).offset(skip).limit(limit).all()


def create_team(db: Session, team: schemas.CreateTeam):
    new_team = models.Team(team_name=team.team_name, country_id=team.country_id)
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return new_team

def update_team_by_id(db: Session, team_id, team):
    db_team = get_team_by_id(db, team_id=team_id)
    db_team.team_name = team.team_name
    db_team.country_id = team.country_id
    db.commit()
    db.refresh(db_team)
    return db_team


def delete_team_by_id(db: Session, team_id: int):
    deleted_team = db.query(models.Team).filter(models.Team.id == team_id).first()
    db.delete(deleted_team)
    db.commit()
    return deleted_team
