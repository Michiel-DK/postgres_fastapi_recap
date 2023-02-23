from sqlalchemy.orm import Session

from . import models, schemas

def get_all_airbnb(db: Session, city:str):
    return db.query(models.Airbnb).filter(models.Airbnb.city == city).all()