from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from player_role import player_role_schema, player_role_curd
from dependencies import get_db

router = APIRouter()


@router.get("/player_role/{player_role_id}", response_model=player_role_schema.BasePlayerRole, tags=['Player Role'])
def read_player_role_by_id(player_role_id: int, db: Session = Depends(get_db)):
    db_player_role = player_role_curd.get_player_role_by_id(db, player_role_id=player_role_id)
    if db_player_role is None:
        raise HTTPException(status_code=404, detail="Player role not found")
    return db_player_role


@router.get("/player_roles/", response_model=List[player_role_schema.BasePlayerRole], tags=['Player Role'])
def read_player_role(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    countries = player_role_curd.get_player_roles(db, skip=skip, limit=limit)
    return countries


@router.post("/new_player_role/", response_model=player_role_schema.BasePlayerRole, tags=['Player Role'])
def create_player_role(player_role: player_role_schema.CreatePlayerRole, db: Session = Depends(get_db)):
    db_user = player_role_curd.create_player_role(db, player_role)
    if db_user:
        raise HTTPException(status_code=200, detail="Player role created")
    return player_role_curd.create_player_role(db, player_role)


@router.patch("/update_player_role/{player_role_id}", response_model=player_role_schema.UpdatePlayerRole, tags=['Player Role'])
def update_player_role(player_role_id: int, player_role: player_role_schema.UpdatePlayerRole, db: Session = Depends(get_db)):
    updated_player_role = player_role_curd.update_player_role_by_id(db, player_role_id, player_role)
    if updated_player_role is None:
        raise HTTPException(status_code=404, detail="Player role not found")
    return updated_player_role


@router.delete("/delete_player_role/{player_role_id}", response_model=player_role_schema.BasePlayerRole, tags=['Player Role'])
def delete_player_role_by_id(player_role_id: int, db: Session = Depends(get_db)):
    db_player_role = player_role_curd.delete_player_role_by_id(db, player_role_id=player_role_id)
    if db_player_role is None:
        raise HTTPException(status_code=404, detail="Player role not found")
    return db_player_role
