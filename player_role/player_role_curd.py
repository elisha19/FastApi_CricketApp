from sqlalchemy.orm import Session
from database import engine
from player_role import player_role_schema as schemas, player_role_model as models

models.Base.metadata.create_all(bind=engine)


def get_player_role_by_id(db: Session, player_role_id: int):
    return db.query(models.PlayerRole).filter(models.PlayerRole.id == player_role_id).first()


def get_player_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PlayerRole).offset(skip).limit(limit).all()


def create_player_role(db: Session, player_role: schemas.CreatePlayerRole):
    new_player_role = models.PlayerRole(role_name=player_role.role_name)
    db.add(new_player_role)
    db.commit()
    db.refresh(new_player_role)
    return new_player_role

def update_player_role_by_id(db: Session, player_role_id, player_role):
    db_player_role = get_player_role_by_id(db, player_role_id=player_role_id)
    db_player_role.role_name = player_role.role_name
    db.commit()
    db.refresh(db_player_role)
    return db_player_role


def delete_player_role_by_id(db: Session, player_role_id: int):
    deleted_player_role = db.query(models.PlayerRole).filter(models.PlayerRole.id == player_role_id).first()
    db.delete(deleted_player_role)
    db.commit()
    return deleted_player_role
