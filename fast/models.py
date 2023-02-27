from sqlalchemy import Boolean, Column, Integer, String, Float

from sqlalchemy.ext.declarative import declarative_base

#returns a class to create Base class => from this class to create each of the database models or classes
Base = declarative_base()

class Airbnb(Base):
    
    """
    In this context a data-model is pythonic representation of a database table.
    
    We are inheriting from the Base class to have a class-based representation of tables. Each property or attribute of this class is translated into a column in the table
    
    Shoul be only per database table -> you can change the output in the schemas
    
    """
    
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, primary_key=False, index=False)
    room_price = Column(Float, primary_key=False, index=False)
    host_is_superhost = Column(Boolean, primary_key=False, index=False)
    bedrooms = Column(Integer, primary_key=False, index=True)
    satisfaction = Column(Float, primary_key=False, index=False)