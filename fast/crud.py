from sqlalchemy.orm import Session

from . import models, schemas

def get_all_airbnb(db: Session, city:str):
    """
    Read function that depends on database and city:
    - queries the Airbnb data model
    - filters on a user-provided city
    - then returns all observations in database 
    """
    return db.query(models.Airbnb).filter(models.Airbnb.city == city).all()