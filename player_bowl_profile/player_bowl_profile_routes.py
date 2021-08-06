from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from dependencies import get_db
from . import player_bowl_profile_curd as bowl_curd
from . import player_bowl_profile_schema as bowl_schema

router = APIRouter()


@router.get("/player_bowl_profile/{player_bowl_id}", response_model=bowl_schema.BasePlayerBowlProfile, tags=['Player Bowl Profile'])
def read_player_bowl_profile_by_id(player_bowl_id: int, db: Session = Depends(get_db)):
    db_player_bowl = bowl_curd.get_player_bowl_profile_by_id(db, player_bowl_id)
    if db_player_bowl is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return db_player_bowl


@router.get("/player_bowl_profiles/", response_model=List[bowl_schema.BasePlayerBowlProfile], tags=['Player Bowl Profile'])
def read_player_bowl_profile(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    player_bowl_profiles = bowl_curd.get_player_bowl_profiles(db, skip=skip, limit=limit)
    return player_bowl_profiles


@router.post("/new_player_bowl_profile/", response_model=bowl_schema.BasePlayerBowlProfile, tags=['Player Bowl Profile'])
def create_player_bowl_profile(bowl_profile: bowl_schema.CreatePlayerBowlProfile, db: Session = Depends(get_db)):
    db_bowl_profile = bowl_curd.create_player_bowl_profile(db, bowl_profile)
    if db_bowl_profile:
        raise HTTPException(status_code=200, detail="Match Created")
    return bowl_curd.create_player_bowl_profile(db, bowl_profile)


@router.patch("/update_player_bowl_profile/{player_bowl_profile_id}", response_model=bowl_schema.UpdatePlayerBowlProfile, tags=['Player Bowl Profile'])
def update_player_bowl_profile(player_bowl_profile_id: int, player_bowl_profile: bowl_schema.UpdatePlayerBowlProfile, db: Session = Depends(get_db)):
    updated_player_bowl_profile = bowl_curd.update_player_bowl_profile_by_id(db, player_bowl_profile_id, player_bowl_profile)
    if updated_player_bowl_profile is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return updated_player_bowl_profile


@router.delete("/delete_player_bowl_profile/{player_bowl_profile_id}", response_model=bowl_schema.BasePlayerBowlProfile, tags=['Player Bowl Profile'])
def delete_player_bowl_profile_by_id(player_bowl_profile_id: int, db: Session = Depends(get_db)):
    db_player_bowl_profile = bowl_curd.delete_player_bowl_profile_by_id(db, player_bowl_profile_id)
    if db_player_bowl_profile is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return db_player_bowl_profile
