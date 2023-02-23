from typing import Optional
from pydantic import BaseModel

class AirbnbBase(BaseModel):
    #needs to be returned
    id: int
    #optional to potentially return nan
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
        