from sqlalchemy.orm import Session
from match_summary import match_summary_model as models
from match_summary import match_summary_schema as schemas


def get_match_summary_by_id(db: Session, match_summary_id: int):
    return db.query(models.MatchSummary).filter(models.MatchSummary.id == match_summary_id).first()


def get_match_summaries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MatchSummary).offset(skip).limit(limit).all()


def create_match_summary(db: Session, match_summary: schemas.CreateMatchSummary):
    new_match_summary = models.MatchSummary(team_1_id=match_summary.team_1_id,
                                            team_2_id=match_summary.team_2_score,
                                            captain_player_1_id=match_summary.captain_player_1_id,
                                            captain_player_2_id=match_summary.captain_player_2_id,
                                            man_of_match_player_id=match_summary.man_of_match_player_id,
                                            bowler_of_match_player_id=match_summary.bowler_of_match_player_id,
                                            winner_team_id=match_summary.winner_team_id,
                                            loser_team_id=match_summary.loser_team_id,
                                            team_1_score=match_summary.team_1_score,
                                            team_2_score=match_summary.team_1_score,
                                            team_1_wicket=match_summary.team_1_wicket,
                                            team_2_wicket=match_summary.team_2_wicket,
                                            first_inning_team_id=match_summary.first_inning_team_id,
                                            match_result_type_id=match_summary.match_result_type_id,
                                            match_id=match_summary.match_id)
    db.add(new_match_summary)
    db.commit()
    db.refresh(new_match_summary)
    return new_match_summary


def update_match_summary_by_id(db: Session, match_summary_id, match_summary):
    db_match_summary = get_match_summary_by_id(db, match_summary_id=match_summary_id)

    db_match_summary.team_1_id = match_summary.team_1_id
    db_match_summary.team_2_score = match_summary.team_2_score
    db_match_summary.captain_player_1_id = match_summary.captain_player_1_id
    db_match_summary.captain_player_2_id = match_summary.captain_player_2_id
    db_match_summary.man_of_match_player_id = match_summary.man_of_match_player_id
    db_match_summary.bowler_of_match_player_id = match_summary.bowler_of_match_player_id
    db_match_summary.winner_team_id = match_summary.winner_team_id
    db_match_summary.loser_team_id = match_summary.loser_team_id
    db_match_summary.team_1_score = match_summary.team_1_score
    db_match_summary.team_2_score = match_summary.team_2_score
    db_match_summary.team_1_wicket = match_summary.team_1_wicket
    db_match_summary.team_2_wicket = match_summary.team_2_wicket
    db_match_summary.first_inning_team_id = match_summary.first_inning_team_id
    db_match_summary.match_result_type_id = match_summary.match_result_type_id
    db_match_summary.match_id = match_summary.match_id

    db.commit()
    db.refresh(db_match_summary)
    return db_match_summary


def delete_team_by_id(db: Session, match_summary_id: int):
    deleted_match_summary = db.query(models.MatchSummary).filter(models.MatchSummary.id == match_summary_id).first()
    db.delete(deleted_match_summary)
    db.commit()
    return deleted_match_summary
