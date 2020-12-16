from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class DogSchema(BaseModel):
    id: str    
    

class DogDB(DogSchema):
    name: str 
    picture: Optional[str]
    is_adopted: Optional[bool]
    user_id: Optional[int]
    created_date: Optional[datetime]
 
    
class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str

class UserDB(UserSchema):
    created_date: Optional[datetime]


class AdoptSchema(BaseModel):
    dog_name: str
    user_id: int