from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from dependencies import get_db
from player_bat_profile import player_bat_profile_curd as bat_curd
from player_bat_profile import player_bat_profile_schema as bat_schema

router = APIRouter()

@router.get("/player_bat_profile/{player_bat_id}", response_model=bat_schema.BasePlayerBatProfile, tags=['Player Bat Profile'])
def read_player_bat_profile_by_id(player_bat_id: int, db: Session = Depends(get_db)):
    db_player_bat = bat_curd.get_player_bat_profile_by_id(db, player_bat_id)
    if db_player_bat is None:
        raise HTTPException(status_code=404, detail="Player bat profile not found")
    return db_player_bat


@router.get("/player_bat_profiles/", response_model=List[bat_schema.BasePlayerBatProfile], tags=['Player Bat Profile'])
def read_player_bat_profile(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    player_bat_profiles = bat_curd.get_player_bat_profiles(db, skip=skip, limit=limit)
    return player_bat_profiles


@router.post("/new_player_bat_profile/", response_model=bat_schema.BasePlayerBatProfile, tags=['Player Bat Profile'])
def create_player_bat_profile(bat_profile: bat_schema.CreatePlayerBatProfile, db: Session = Depends(get_db)):
    db_bat_profile = bat_curd.create_new_player_bat_profile(db, bat_profile)
    if db_bat_profile:
        raise HTTPException(status_code=200, detail="Player bat profile Created")
    return bat_curd.create_new_player_bat_profile(db, bat_profile)


@router.patch("/update_player_bat_profile/{player_bat_profile_id}", response_model=bat_schema.UpdatePlayerBatProfile, tags=['Player Bat Profile'])
def update_player_bat_profile(player_bat_profile_id: int, player_bat_profile: bat_schema.UpdatePlayerBatProfile, db: Session = Depends(get_db)):
    updated_player_bat_profile = bat_curd.update_player_bat_profile_by_id(db, player_bat_profile_id, player_bat_profile)
    if updated_player_bat_profile is None:
        raise HTTPException(status_code=404, detail="Player bat profile not found")
    return updated_player_bat_profile


@router.delete("/delete_player_bat_profile/{player_bat_profile_id}", response_model=bat_schema.BasePlayerBatProfile, tags=['Player Bat Profile'])
def delete_player_bat_profile_by_id(player_bat_profile_id: int, db: Session = Depends(get_db)):
    db_player_bat_profile = bat_curd.delete_player_bat_profile_by_id(db, player_bat_profile_id)
    if db_player_bat_profile is None:
        raise HTTPException(status_code=404, detail="Player bat profile not found")
    return db_player_bat_profile
