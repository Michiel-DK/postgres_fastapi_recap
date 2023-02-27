from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fast.params import *

'''setup engine - connection to DB in container'''
engine = create_engine(
    POSTGRES_URI, echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

'''use to create independent db sessions for each request'''
def get_db():
    #instance of the SessionLocal class => the actual database session
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()