from sqlalchemy.orm import Session
from . import player_bat_profile_model as model
from . import player_bat_profile_schema as schemas


def get_player_bat_profile_by_id(db: Session, player_bat_profile_id: int):
    return db.query(model.PlayerBatProfile).filter(model.PlayerBatProfile.id == player_bat_profile_id).first()


def get_player_bat_profiles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.PlayerBatProfile).offset(skip).limit(limit).all()


def create_new_player_bat_profile(db: Session, player_bat_profile: schemas.CreatePlayerBatProfile):
    new_match_profile = model.PlayerBatProfile(matches=player_bat_profile.matches,
                                               innings=player_bat_profile.innings,
                                               no_of_not_outs=player_bat_profile.no_of_not_outs,
                                               runs=player_bat_profile.runs,
                                               highest_score=player_bat_profile.highest_score,
                                               average=player_bat_profile.average,
                                               no_of_balls_faced=player_bat_profile.no_of_balls_faced,
                                               strike_rate=player_bat_profile.strike_rate,
                                               half_centuries=player_bat_profile.half_centuries,
                                               full_centuries=player_bat_profile.full_centuries,
                                               boundaries=player_bat_profile.boundaries,
                                               sixes=player_bat_profile.sixes,
                                               player_id=player_bat_profile.player_id)

    db.add(new_match_profile)
    db.commit()
    db.refresh(new_match_profile)
    return new_match_profile


def update_player_bat_profile_by_id(db: Session, player_bat_profile_id, player_bat_profile):
    db_player_bat_profile = get_player_bat_profile_by_id(db, player_bat_profile_id=player_bat_profile_id)

    db_player_bat_profile.matches = player_bat_profile.matches
    db_player_bat_profile.innings = player_bat_profile.innings
    db_player_bat_profile.no_of_not_outs = player_bat_profile.no_of_not_outs
    db_player_bat_profile.runs = player_bat_profile.runs
    db_player_bat_profile.highest_score = player_bat_profile.highest_score
    db_player_bat_profile.average = player_bat_profile.average
    db_player_bat_profile.no_of_balls_faced = player_bat_profile.no_of_balls_faced
    db_player_bat_profile.strike_rate = player_bat_profile.strike_rate
    db_player_bat_profile.half_centuries = player_bat_profile.half_centuries
    db_player_bat_profile.full_centuries = player_bat_profile.full_centuries
    db_player_bat_profile.boundaries = player_bat_profile.boundaries
    db_player_bat_profile.sixes = player_bat_profile.sixes
    db_player_bat_profile.player_id = player_bat_profile.player_id

    db.commit()
    db.refresh(db_player_bat_profile)
    return db_player_bat_profile


def delete_player_bat_profile_by_id(db: Session, player_bat_profile_id: int):
    deleted_player_bat_profile = db.query(model.PlayerBatProfile).filter(model.PlayerBatProfile.id == player_bat_profile_id).first()
    db.delete(deleted_player_bat_profile)
    db.commit()
    return deleted_player_bat_profile
