from sqlalchemy import Column, Integer, ForeignKey
from database import Base

class MatchSummary(Base):
    __tablename__ = "MatchSummary"

    id = Column(Integer, primary_key=True)
    team_1_id = Column(Integer)
    team_2_id = Column(Integer)
    captain_player_1_id = Column(Integer)
    captain_player_2_id = Column(Integer)
    man_of_match_player_id = Column(Integer)
    bowler_of_match_player_id = Column(Integer)
    winner_team_id = Column(Integer)
    loser_team_id = Column(Integer)
    team_1_score = Column(Integer)
    team_2_score = Column(Integer)
    team_1_wicket = Column(Integer)
    team_2_wicket = Column(Integer)
    first_inning_team_id = Column(Integer)
    match_result_type_id = Column(Integer)
    match_id = Column(Integer, ForeignKey('Match.id'))
