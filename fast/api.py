from fastapi import FastAPI
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
#from jose import JWTError, jwt
from typing import List
from sqlalchemy.orm import Session
from . import crud, schemas
# from .database import SessionLocal
# import os
# from dotenv import load_dotenv
# from datetime import timedelta
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
    return {'greeting': 'hi'}

@app.get("/airbnb/{city}", response_model=List[schemas.Airbnb])
def read_items(city: str, db: Session = Depends(get_db)):
    items = crud.get_all_airbnb(db, city=city)
    return items
