from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from . import player_curd
from . import player_schema
from dependencies import get_db

router = APIRouter()

@router.get("/player/{player_id}", response_model=player_schema.BasePlayer, tags=['Player'])
def read_player_by_id(player_id: int, db: Session = Depends(get_db)):
    db_player = player_curd.get_player_by_id(db, player_id=player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player


@router.get("/players/", response_model=List[player_schema.BasePlayer], tags=['Player'])
def read_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    players = player_curd.get_players(db, skip=skip, limit=limit)
    return players


@router.post("/new_player/", response_model=player_schema.BasePlayer, tags=['Player'])
def create_player(player: player_schema.CreatePlayer, db: Session = Depends(get_db)):
    db_user = player_curd.create_player(db, player)
    if db_user:
        raise HTTPException(status_code=200, detail="Player Created")
    return player_curd.create_player(db, player)


@router.patch("/update_player/{player_id}", response_model=player_schema.UpdatePlayer, tags=['Player'])
def update_player(player_id: int, player: player_schema.UpdatePlayer, db: Session = Depends(get_db)):
    updated_player = player_curd.update_player_by_id(db, player_id, player)
    if updated_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return updated_player


@router.delete("/delete_player/{player_id}", response_model=player_schema.BasePlayer, tags=['Player'])
def delete_player_by_id(player_id: int, db: Session = Depends(get_db)):
    db_player = player_curd.get_player_by_id(db, player_id=player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player
