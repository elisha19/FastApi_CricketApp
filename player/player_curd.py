from sqlalchemy.orm import Session
from . import player_model as models
from . import player_schema as schemas


def get_player_by_id(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()


def get_players(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Player).offset(skip).limit(limit).all()


def create_player(db: Session, player: schemas.CreatePlayer):
    new_player = models.Player(name=player.name,
                               age=player.age,
                               dob=player.dob,
                               retirement_date=player.retirement_date,
                               player_role_id=player.player_role_id,
                               team_id=player.team_id)

    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player


def update_player_by_id(db: Session, player_id, player):
    db_player = get_player_by_id(db, player_id=player_id)

    db_player.name = player.name
    db_player.age = player.age
    db_player.dob = player.dob
    db_player.retirement_date = player.retirement_date
    db_player.player_role_id = player.player_role_id
    db_player.team_id = player.team_id

    db.commit()
    db.refresh(db_player)
    return db_player


def delete_player_by_id(db: Session, player_id: int):
    deleted_player = db.query(models.Player).filter(models.Player.id == player_id).first()
    db.delete(deleted_player)
    db.commit()
    return deleted_player
