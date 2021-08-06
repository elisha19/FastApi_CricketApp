from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from match_result import match_result_schema, match_result_curd
from dependencies import get_db

router = APIRouter()


@router.get("/match_result/{match_result_id}", response_model=match_result_schema.BaseMatchResult, tags=['Match Result'])
def read_match_result_by_id(match_result_id: int, db: Session = Depends(get_db)):
    db_match_result = match_result_curd.get_match_result_by_id(db, match_result_id=match_result_id)
    if db_match_result is None:
        raise HTTPException(status_code=404, detail="MatchResult not found")
    return db_match_result


@router.get("/match_results/", response_model=List[match_result_schema.BaseMatchResult], tags=['Match Result'])
def read_match_results(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    match_results = match_result_curd.get_match_results(db, skip=skip, limit=limit)
    return match_results


@router.post("/new_match_result/", response_model=match_result_schema.BaseMatchResult, tags=['Match Result'])
def create_match_result(match_result: match_result_schema.CreateMatchResult, db: Session = Depends(get_db)):
    db_user = match_result_curd.create_match_result(db, match_result)
    if db_user:
        raise HTTPException(status_code=200, detail="MatchResult Created")
    return match_result_curd.create_match_result(db, match_result)


@router.patch("/update_match_result/{match_result_id}", response_model=match_result_schema.UpdateMatchResult, tags=['Match Result'])
def update_match_result(match_result_id: int, match_result: match_result_schema.UpdateMatchResult, db: Session = Depends(get_db)):
    updated_match_result = match_result_curd.update_match_result_by_id(db, match_result_id, match_result)
    if updated_match_result is None:
        raise HTTPException(status_code=404, detail="MatchResult not found")
    return updated_match_result


@router.delete("/delete_match_result/{match_result_id}", response_model=match_result_schema.BaseMatchResult, tags=['Match Result'])
def delete_match_result_by_id(match_result_id: int, db: Session = Depends(get_db)):
    db_match_result = match_result_curd.delete_match_result_by_id(db, match_result_id=match_result_id)
    if db_match_result is None:
        raise HTTPException(status_code=404, detail="MatchResult not found")
    return db_match_result
