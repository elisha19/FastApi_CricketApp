from fastapi import Depends, FastAPI
from country import country_routes as country
from match_result import match_result_routes as match_result
from match_type import match_type_routes as match_type
from player_role import player_role_routes as player_role
from match import match_routes as match
from match_summary import match_summary_routes as match_summary
from player_bat_profile import player_bat_profile_routes as player_bat_profile
from player_bowl_profile import player_bowl_profile_routes as player_bowl_profile
from player import player_routes as player
from team import team_routes as team
from team_profile import team_profile_routes as team_profile
from tournament import tournament_routes as tournament
from venue import venue_routes as venue
# from dependencies import get_query_token


# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()


@app.get("/")
async def root():
    return {
        "Application": "Cricket League Rest API",
    }


# country routes
app.include_router(country.router)

# match routes
app.include_router(match.router)

# match result routes
app.include_router(match_result.router)

# match type result routes
app.include_router(match_type.router)

# match summary routes
app.include_router(match_summary.router)

# player role routes
app.include_router(player_role.router)

# player bat profile routes
app.include_router(player_bat_profile.router)

# player bowl profile routes
app.include_router(player_bowl_profile.router)

# player routes
app.include_router(player.router)

# team summary routes
app.include_router(team.router)

# team profile routes
app.include_router(team_profile.router)

# tournament routes
app.include_router(tournament.router)

# venue routes
app.include_router(venue.router)


