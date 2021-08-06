from pydantic import BaseModel


class BaseMatchSummary(BaseModel):
    team_1_id: int
    team_2_id: int
    captain_player_1_id: int
    captain_player_2_id: int
    man_of_match_player_id: int
    bowler_of_match_player_id: int
    winner_team_id: int
    loser_team_id: int
    team_1_score: int
    team_2_score: int
    team_1_wicket: int
    team_2_wicket: int
    first_inning_team_id: int
    match_result_type_id: int
    match_id: int

    class Config:
        orm_mode = True


class CreateMatchSummary(BaseMatchSummary):
    pass


class UpdateMatchSummary(BaseMatchSummary):
    pass


class MatchSummary(BaseMatchSummary):
    id: int

