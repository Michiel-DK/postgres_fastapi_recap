from fastapi import FastAPI
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import get_db

app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get('/')
def root():
    return "{'greeting': 'hi'}"


@app.get("/airbnb_pricing/{city}", response_model=List[schemas.AirbnbPricing])
def read_items(city: str, db: Session = Depends(get_db)):
    """ 
    Get request which:
    - takes in city as an argument -> options: amsterdam, athens, barcelona, berlin, budapest, lisbon, london, paris, rome, vienna
    - responds with the airbnb PRICING schema as a list for all rows
    """
    items = crud.get_all_airbnb(db, city=city)
    return items

@app.get("/airbnb_other/{city}", response_model=List[schemas.AirbnbOther])
def read_items(city: str, db: Session = Depends(get_db)):
    """ 
    Get request which:
    - takes in city as an argument -> options: amsterdam, athens, barcelona, berlin, budapest, lisbon, london, paris, rome, vienna
    - responds with the airbnb OTHER schema as a list for all rows
    """
    items = crud.get_all_airbnb(db, city=city)
    return items