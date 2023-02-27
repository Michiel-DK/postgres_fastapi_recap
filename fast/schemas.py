from typing import Optional
from pydantic import BaseModel

class AirbnbBase(BaseModel):
    
    '''
    Shemas are used to:
    - validate data we receive as well
    - reformat the data that we want to send to the client
    
    We're inheriting the BaseModel from pydantic to suggest validation errors to users.
    
    '''
    
    #needs to be returned
    id: int
    
    #optional to return
    city: Optional[str] = None
    room_price: Optional[float] = None
    host_is_superhost: Optional[bool] = None
    bedrooms : Optional[int] = None
    satisfaction: Optional[float] = None
    
class Airbnb(AirbnbBase):
    id: int
    city:str

    class Config:
        #orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
        orm_mode = True
        