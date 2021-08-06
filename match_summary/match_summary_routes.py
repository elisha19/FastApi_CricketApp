from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from match_summary import match_summary_schema as schemas, match_summary_curd as curd
from dependencies import get_db


router = APIRouter()


@router.get("/match_summary/{match_summary_id}", response_model=schemas.BaseMatchSummary, tags=['Match Summary'])
def read_match_summary_by_id(match_id: int, db: Session = Depends(get_db)):
    db_match = curd.get_match_summary_by_id(db, match_id)
    if db_match is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return db_match


@router.get("/match_summaries/", response_model=List[schemas.BaseMatchSummary], tags=['Match Summary'])
def read_matches_summary(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    matches = curd.get_match_summaries(db, skip=skip, limit=limit)
    if matches is None:
        raise HTTPException(status_code=404, detail="No matches")
    return matches


@router.post("/new_match_summary/", response_model=schemas.BaseMatchSummary, tags=['Match Summary'])
def create_match_summary(match: schemas.CreateMatchSummary, db: Session = Depends(get_db)):
    new_match = curd.create_match_summary(db, match)
    if new_match:
        raise HTTPException(status_code=200, detail="Match Created")
    return curd.create_match_summary(db, match)


@router.patch("/update_match_summary/{update_match_summary_id}", response_model=schemas.UpdateMatchSummary, tags=['Match Summary'])
def update_match_summary(match_id: int, match_summary: schemas.UpdateMatchSummary, db: Session = Depends(get_db)):
    updated_match = curd.update_match_summary_by_id(db, match_id, match_summary)
    if updated_match is None:
        raise HTTPException(status_code=404, detail="MatchResult not found")
    return updated_match


@router.delete("/delete_match_summary/{match_id}", response_model=schemas.BaseMatchSummary, tags=['Match Summary'])
def delete_match_by_id(match_id: int, db: Session = Depends(get_db)):
    db_match = curd.delete_team_by_id(db, match_id)
    if db_match is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return db_match
