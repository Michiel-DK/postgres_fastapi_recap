from typing import Optional
from pydantic import BaseModel

class AirbnbPricing(BaseModel):
    
    '''
    Shemas are used to:
    - validate data we receive as well
    - reformat the data that we want to send to the client
    
    We're inheriting the BaseModel from pydantic to suggest validation errors to users.
    
    
    Here we return only PRICING data from the model
    
    '''
    
    #needs to be returned
    id: int
    city: str
    
    #optional to return
    room_price: Optional[float] = None
    
    class Config:
        #orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
        orm_mode = True
    
class AirbnbOther(BaseModel):
    
    '''
    Shemas are used to:
    - validate data we receive as well
    - reformat the data that we want to send to the client
    
    We're inheriting the BaseModel from pydantic to suggest validation errors to users.
    
    
    Here we return only OTHER data from the model
    
    '''
    
    #needs to be returned
    id: int
    city: str
    
    #optional to return
    host_is_superhost: Optional[bool] = None
    bedrooms : Optional[int] = None
    satisfaction: Optional[float] = None
    
    class Config:
        #orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
        orm_mode = True

        