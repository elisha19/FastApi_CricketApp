from sqlalchemy.orm import Session
from . import player_bowl_profile_model as model
from . import player_bowl_profile_schema as schemas


def get_player_bowl_profile_by_id(db: Session, player_bowl_profile_id: int):
    return db.query(model.PlayerBowlProfile).filter(model.PlayerBowlProfile.id == player_bowl_profile_id).first()


def get_player_bowl_profiles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.PlayerBowlProfile).offset(skip).limit(limit).all()


def create_player_bowl_profile(db: Session, player_bowl_profile: schemas.CreatePlayerBowlProfile):
    new_player_bowl_profile = model.PlayerBowlProfile(matches=player_bowl_profile.matches,
                                                      innings=player_bowl_profile.innings,
                                                      no_of_deliveries=player_bowl_profile.no_of_deliveries,
                                                      runs=player_bowl_profile.runs,
                                                      wickets=player_bowl_profile.wickets,
                                                      best_bowling_in_match=player_bowl_profile.best_bowling_in_match,
                                                      economy=player_bowl_profile.economy,
                                                      average=player_bowl_profile.average,
                                                      SR=player_bowl_profile.SR,
                                                      W5=player_bowl_profile.W5,
                                                      W10=player_bowl_profile.W10,
                                                      player_id=player_bowl_profile.player_id)

    db.add(new_player_bowl_profile)
    db.commit()
    db.refresh(new_player_bowl_profile)
    return new_player_bowl_profile


def update_player_bowl_profile_by_id(db: Session, player_bowl_profile_id, player_bowl_profile):
    db_player_bowl_profile = get_player_bowl_profile_by_id(db, player_bowl_profile_id=player_bowl_profile_id)

    db_player_bowl_profile.matches = player_bowl_profile.matches
    db_player_bowl_profile.innings = player_bowl_profile.innings
    db_player_bowl_profile.no_of_not_outs = player_bowl_profile.no_of_not_outs
    db_player_bowl_profile.runs = player_bowl_profile.runs
    db_player_bowl_profile.highest_score = player_bowl_profile.highest_score
    db_player_bowl_profile.average = player_bowl_profile.average
    db_player_bowl_profile.no_of_balls_faced = player_bowl_profile.no_of_balls_faced
    db_player_bowl_profile.strike_rate = player_bowl_profile.strike_rate
    db_player_bowl_profile.half_centuries = player_bowl_profile.half_centuries
    db_player_bowl_profile.full_centuries = player_bowl_profile.full_centuries
    db_player_bowl_profile.boundaries = player_bowl_profile.boundaries
    db_player_bowl_profile.sixes = player_bowl_profile.sixes
    db_player_bowl_profile.player_id = player_bowl_profile.player_id

    db.commit()
    db.refresh(db_player_bowl_profile)
    return db_player_bowl_profile


def delete_player_bowl_profile_by_id(db: Session, player_bowl_profile_id: int):
    deleted_player_bowl_profile = db.query(model.PlayerBowlProfile).filter(
        model.PlayerBowlProfile.id == player_bowl_profile_id).first()
    db.delete(deleted_player_bowl_profile)
    db.commit()
    return deleted_player_bowl_profile
