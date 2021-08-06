from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from country import country_schema, country_curd
from dependencies import get_db

router = APIRouter()


@router.get("/country/{country_id}", response_model=country_schema.BaseCountry, tags=['Country'])
def read_country_by_id(country_id: int, db: Session = Depends(get_db)):
    db_country = country_curd.get_country_by_id(db, country_id=country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_country


@router.get("/countries/", response_model=List[country_schema.BaseCountry], tags=['Country'])
def read_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    countries = country_curd.get_countries(db, skip=skip, limit=limit)
    return countries


@router.post("/new_country/", response_model=country_schema.BaseCountry, tags=['Country'])
def create_country(country: country_schema.CreateCountry, db: Session = Depends(get_db)):
    db_user = country_curd.create_country(db, country)
    if db_user:
        raise HTTPException(status_code=200, detail="Country Created")
    return country_curd.create_country(db, country)


@router.patch("/update_country/{country_id}", response_model=country_schema.UpdateCountry, tags=['Country'])
def update_country(country_id: int, country: country_schema.UpdateCountry, db: Session = Depends(get_db)):
    updated_country = country_curd.update_country_by_id(db, country_id, country)
    if updated_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return updated_country


@router.delete("/delete_country/{country_id}", response_model=country_schema.BaseCountry, tags=['Country'])
def delete_country_by_id(country_id: int, db: Session = Depends(get_db)):
    db_country = country_curd.delete_country_by_id(db, country_id=country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_country
