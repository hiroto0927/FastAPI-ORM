from pydantic import BaseModel,Field
from typing import Optional

class CreateMember(BaseModel):
    name: str 
    age:int
    dep_id:int

    class Config:
        orm_mode = True

class Member(CreateMember):
    id: int

class UpdateMember(BaseModel):
    name: Optional[str]  = Field(min_length=1,max_length=12)
    age: Optional[int]
    dep_id: Optional[int] 

    class Config:
        orm_mode = True