from sqlalchemy import Boolean, Column, Integer, String, Float

from .database import Base

class Airbnb(Base):
    __tablename__ = "airbnb"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, primary_key=False, index=False)
    room_price = Column(Float, primary_key=False, index=False)
    host_is_superhost = Column(Boolean, primary_key=False, index=False)
    bedrooms = Column(Integer, primary_key=False, index=True)
    satisfaction = Column(Float, primary_key=False, index=False)