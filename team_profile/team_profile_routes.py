from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from . import team_profile_curd, team_profile_schema as schema
from dependencies import get_db

router = APIRouter()

@router.get("/team_profile/{team_profile_id}", response_model=schema.BaseTeamProfile, tags=['Team Profile'])
def read_team_profile_by_id(team_profile_id: int, db: Session = Depends(get_db)):
    db_team_profile = team_profile_curd.get_team_profile_by_id(db, team_profile_id=team_profile_id)
    if db_team_profile is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return db_team_profile


@router.get("/team_profiles/", response_model=List[schema.BaseTeamProfile], tags=['Team Profile'])
def read_team_profiles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teams = team_profile_curd.get_team_profiles(db, skip=skip, limit=limit)
    return teams


@router.post("/new_team_profile/", response_model=schema.BaseTeamProfile, tags=['Team Profile'])
def create_team_profile(team: schema.CreateTeamProfile, db: Session = Depends(get_db)):
    new_team_profile = team_profile_curd.create_team_profile(db, team)
    if new_team_profile:
        raise HTTPException(status_code=200, detail="Team profile Created")
    return new_team_profile.create_team(db, team)


@router.patch("/update_team_profile/{team_profile_id}", response_model=schema.BaseTeamProfile, tags=['Team Profile'])
def update_team(team_profile_id: int, team_profile: schema.UpdateTeamProfile, db: Session = Depends(get_db)):
    updated_team_profile = team_profile_curd.update_team_profile_by_id(db, team_profile_id, team_profile)
    if updated_team_profile is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return updated_team_profile


@router.delete("/delete_profile_team/{team_profile_id}", response_model=schema.BaseTeamProfile, tags=['Team Profile'])
def delete_team_profile_by_id(team_profile_id: int, db: Session = Depends(get_db)):
    db_team_profile = team_profile_curd.delete_team_profile_by_id(db, team_profile_id=team_profile_id)
    if db_team_profile is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return db_team_profile
