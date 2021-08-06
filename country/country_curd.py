from sqlalchemy.orm import Session
from database import engine
from country import country_schema as schemas, country_model as models

models.Base.metadata.create_all(bind=engine)


def get_country_by_id(db: Session, country_id: int):
    return db.query(models.Country).filter(models.Country.id == country_id).first()


def get_countries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Country).offset(skip).limit(limit).all()


def create_country(db: Session, country: schemas.CreateCountry):
    new_country = models.Country(country_name=country.country_name)
    db.add(new_country)
    db.commit()
    db.refresh(new_country)
    return new_country

def update_country_by_id(db: Session, country_id, country):
    db_country = get_country_by_id(db, country_id=country_id)
    db_country.country_name = country.country_name
    db.commit()
    db.refresh(db_country)
    return db_country


def delete_country_by_id(db: Session, country_id: int):
    deleted_country = db.query(models.Country).filter(models.Country.id == country_id).first()
    db.delete(deleted_country)
    db.commit()
    return deleted_country
