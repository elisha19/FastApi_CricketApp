from sqlalchemy.orm import Session
from . import tournament_model as models, tournament_schema as schemas


def get_tournament_by_id(db: Session, tournament_id: int):
    return db.query(models.Tournament).filter(models.Tournament.id == tournament_id).first()


def get_tournaments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tournament).offset(skip).limit(limit).all()


def create_tournament(db: Session, tournament: schemas.CreateTournament):
    new_team_profile = models.Tournament(name=tournament.name,
                                         first_place_team_id=tournament.first_place_team_id,
                                         second_place_team_id=tournament.second_place_team_id,
                                         third_place_team_id=tournament.third_place_team_id,
                                         start_date=tournament.start_date,
                                         end_date=tournament.end_date,
                                         total_points=tournament.total_points,
                                         team_id=tournament.team_id)

    db.add(new_team_profile)
    db.commit()
    db.refresh(new_team_profile)
    return new_team_profile


def update_tournament_by_id(db: Session, tournament_id, tournament):
    db_tournament = get_tournament_by_id(db, tournament_id=tournament_id)

    db_tournament.name = tournament.name
    db_tournament.first_place_team_id = tournament.first_place_team_id
    db_tournament.second_place_team_id = tournament.second_place_team_id
    db_tournament.third_place_team_id = tournament.third_place_team_id
    db_tournament.start_date = tournament.start_date
    db_tournament.end_date = tournament.end_date
    db_tournament.total_points = tournament.total_points
    db_tournament.team_id = tournament.team_id

    db.commit()
    db.refresh(db_tournament)
    return db_tournament


def delete_tournament_by_id(db: Session, tournament_id: int):
    deleted_tournament = db.query(models.Tournament).filter(models.Tournament.id == tournament_id).first()
    db.delete(deleted_tournament)
    db.commit()
    return deleted_tournament
