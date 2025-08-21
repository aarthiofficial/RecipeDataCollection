from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .database import SessionLocal
from . import schemas, crud

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/recipes", response_model=dict)
def read_recipes(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    skip = (page - 1) * limit
    recipes = crud.get_recipes(db, skip=skip, limit=limit)
    total = crud.count_recipes(db)
    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": recipes
    }
