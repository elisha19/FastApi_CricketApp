from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from . import tournament_curd
from . import tournament_schema
from dependencies import get_db

router = APIRouter()

@router.get("/tournament/{tournament_id}", response_model=tournament_schema.BaseTournament, tags=['Tournament'])
def read_tournament_by_id(tournament_id: int, db: Session = Depends(get_db)):
    db_tournament = tournament_curd.get_tournament_by_id(db, tournament_id=tournament_id)
    if db_tournament is None:
        raise HTTPException(status_code=404, detail="Tournament not found")
    return db_tournament


@router.get("/tournaments/", response_model=List[tournament_schema.BaseTournament], tags=['Tournament'])
def read_tournaments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tournaments = tournament_curd.get_tournaments(db, skip=skip, limit=limit)
    return tournaments


@router.post("/new_tournament/", response_model=tournament_schema.BaseTournament, tags=['Tournament'])
def create_tournament(tournament: tournament_schema.CreateTournament, db: Session = Depends(get_db)):
    db_user = tournament_curd.create_tournament(db, tournament)
    if db_user:
        raise HTTPException(status_code=200, detail="Tournament Created")
    return tournament_curd.create_tournament(db, tournament)


@router.patch("/update_tournament/{tournament_id}", response_model=tournament_schema.UpdateTournament, tags=['Tournament'])
def update_tournament(tournament_id: int, tournament: tournament_schema.UpdateTournament, db: Session = Depends(get_db)):
    updated_tournament = tournament_curd.update_tournament_by_id(db, tournament_id, tournament)
    if updated_tournament is None:
        raise HTTPException(status_code=404, detail="Tournament not found")
    return updated_tournament


@router.delete("/delete_tournament/{tournament_id}", response_model=tournament_schema.BaseTournament, tags=['Tournament'])
def delete_tournament_by_id(tournament_id: int, db: Session = Depends(get_db)):
    db_tournament = tournament_curd.delete_tournament_by_id(db, tournament_id=tournament_id)
    if db_tournament is None:
        raise HTTPException(status_code=404, detail="Tournament not found")
    return db_tournament
