from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from team import team_schema, team_curd
from dependencies import get_db

router = APIRouter()


@router.get("/team/{team_id}", response_model=team_schema.BaseTeam, tags=['Team'])
def read_team_by_id(team_id: int, db: Session = Depends(get_db)):
    db_team = team_curd.get_team_by_id(db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return db_team


@router.get("/teams/", response_model=List[team_schema.BaseTeam], tags=['Team'])
def read_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teams = team_curd.get_teams(db, skip=skip, limit=limit)
    return teams


@router.post("/new_team/", response_model=team_schema.BaseTeam, tags=['Team'])
def create_team(team: team_schema.CreateTeam, db: Session = Depends(get_db)):
    db_user = team_curd.create_team(db, team)
    if db_user:
        raise HTTPException(status_code=200, detail="Team Created")
    return team_curd.create_team(db, team)


@router.patch("/update_team/{team_id}", response_model=team_schema.UpdateTeam, tags=['Team'])
def update_team(team_id: int, team: team_schema.UpdateTeam, db: Session = Depends(get_db)):
    updated_team = team_curd.update_team_by_id(db, team_id, team)
    if updated_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return updated_team


@router.delete("/delete_team/{team_id}", response_model=team_schema.BaseTeam, tags=['Team'])
def delete_team_by_id(team_id: int, db: Session = Depends(get_db)):
    db_team = team_curd.delete_team_by_id(db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return db_team
