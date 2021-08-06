from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from match_type import match_type_schema, match_type_curd
from dependencies import get_db

router = APIRouter()


@router.get("/match_type/{match_type_id}", response_model=match_type_schema.BaseMatchType, tags=['Match Type'])
def read_match_type_by_id(match_type_id: int, db: Session = Depends(get_db)):
    db_match_type = match_type_curd.get_match_type_by_id(db, match_type_id=match_type_id)
    if db_match_type is None:
        raise HTTPException(status_code=404, detail="MatchType not found")
    return db_match_type


@router.get("/match_types/", response_model=List[match_type_schema.BaseMatchType], tags=['Match Type'])
def read_match_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    match_types = match_type_curd.get_match_types(db, skip=skip, limit=limit)
    return match_types


@router.post("/new_match_type/", response_model=match_type_schema.BaseMatchType, tags=['Match Type'])
def create_match_type(match_type: match_type_schema.CreateMatchType, db: Session = Depends(get_db)):
    db_user = match_type_curd.create_match_type(db, match_type)
    if db_user:
        raise HTTPException(status_code=200, detail="MatchType Created")
    return match_type_curd.create_match_type(db, match_type)


@router.patch("/update_match_type/{match_type_id}", response_model=match_type_schema.UpdateMatchType, tags=['Match Type'])
def update_match_type(match_type_id: int, match_type: match_type_schema.UpdateMatchType, db: Session = Depends(get_db)):
    updated_match_type = match_type_curd.update_match_type_by_id(db, match_type_id, match_type)
    if updated_match_type is None:
        raise HTTPException(status_code=404, detail="MatchType not found")
    return updated_match_type


@router.delete("/delete_match_type/{match_type_id}", response_model=match_type_schema.BaseMatchType, tags=['Match Type'])
def delete_match_type_by_id(match_type_id: int, db: Session = Depends(get_db)):
    db_match_type = match_type_curd.delete_match_type_by_id(db, match_type_id=match_type_id)
    if db_match_type is None:
        raise HTTPException(status_code=404, detail="MatchType not found")
    return db_match_type
