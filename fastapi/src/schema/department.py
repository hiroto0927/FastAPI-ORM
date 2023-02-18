from pydantic import BaseModel
from typing import Optional

class CreateDepartment(BaseModel):
    name: str 

    class Config:
        orm_mode = True

class Department(CreateDepartment):
    id: int

class UpdateDepartment(BaseModel):
    name: Optional[str] 

    class Config:
        orm_mode = True