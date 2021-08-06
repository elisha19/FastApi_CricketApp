from sqlalchemy.orm import Session
from database import engine
from team_profile import team_profile_schema as schemas, team_profile_model as models

models.Base.metadata.create_all(bind=engine)


def get_team_profile_by_id(db: Session, team_profile_id: int):
    return db.query(models.TeamProfile).filter(models.TeamProfile.id == team_profile_id).first()


def get_team_profiles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TeamProfile).offset(skip).limit(limit).all()


def create_team_profile(db: Session, team_profile: schemas.CreateTeamProfile):
    new_team_profile = models.TeamProfile(total_wins=team_profile.total_wins,
                                          total_loses=team_profile.total_loses,
                                          no_of_matches=team_profile.no_of_matches,
                                          rank=team_profile.rank,
                                          team_id=team_profile.team_id)
    db.add(new_team_profile)
    db.commit()
    db.refresh(new_team_profile)
    return new_team_profile

def update_team_profile_by_id(db: Session, team_profile_id, team_profile):
    db_team_profile = get_team_profile_by_id(db, team_profile_id=team_profile_id)

    db_team_profile.total_wins = team_profile.total_wins
    db_team_profile.total_loses = team_profile.total_loses
    db_team_profile.no_of_matches = team_profile.no_of_matches
    db_team_profile.rank = team_profile.rank
    db_team_profile.team_id = team_profile.team_id

    db.commit()
    db.refresh(db_team_profile)
    return db_team_profile


def delete_team_profile_by_id(db: Session, team_profile_id: int):
    deleted_team_profile = db.query(models.TeamProfile).filter(models.TeamProfile.id == team_profile_id).first()
    db.delete(deleted_team_profile)
    db.commit()
    return deleted_team_profile
