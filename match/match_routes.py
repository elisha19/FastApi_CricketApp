from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from match import match_schema, match_curd
from dependencies import get_db

router = APIRouter()

@router.get("/match/{match_id}", response_model=match_schema.BaseMatch, tags=['Match'])
def read_match_by_id(match_id: int, db: Session = Depends(get_db)):
    db_match = match_curd.get_match_by_id(db, match_id)
    if db_match is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return db_match


@router.get("/matches/", response_model=List[match_schema.BaseMatch], tags=['Match'])
def read_matches(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    matches = match_curd.get_matches(db, skip=skip, limit=limit)
    if not matches:
        raise HTTPException(status_code=404, detail="No matches")
    return matches


@router.post("/new_match/", response_model=match_schema.BaseMatch, tags=['Match'])
def create_match(match: match_schema.CreateMatch, db: Session = Depends(get_db)):
    db_match = match_curd.create_match(db, match)
    if db_match:
        raise HTTPException(status_code=200, detail="Match Created")
    return match_curd.create_match(db, match)


@router.patch("/update_match/{match_id}", response_model=match_schema.UpdateMatch, tags=['Match'])
def update_match(match_id: int, match: match_schema.UpdateMatch, db: Session = Depends(get_db)):
    updated_match = match_curd.update_match_by_id(db, match_id, match)
    if updated_match is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return updated_match


@router.delete("/delete_match/{match_id}", response_model=match_schema.BaseMatch, tags=['Match'])
def delete_match_by_id(match_id: int, db: Session = Depends(get_db)):
    db_match = match_curd.delete_match_by_id(db, match_id)
    if db_match is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return db_match
