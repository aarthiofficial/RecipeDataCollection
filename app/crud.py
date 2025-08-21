from sqlalchemy.orm import Session
from . import models

def get_recipes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Recipe).order_by(models.Recipe.rating.desc().nullslast()).offset(skip).limit(limit).all()

def count_recipes(db: Session):
    return db.query(models.Recipe).count()
