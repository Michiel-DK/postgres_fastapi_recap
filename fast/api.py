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


@app.get("/airbnb/{city}", response_model=List[schemas.Airbnb])
def read_items(city: str, db: Session = Depends(get_db)):
    """ 
    Get request which:
    - takes in city as an argument
    - responds with the airbnb schema as a list for all rows
    """
    items = crud.get_all_airbnb(db, city=city)
    return items
