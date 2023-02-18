from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from src.cruds import department
from typing import List
from src.db.database import get_db
from src.schema.department import Department,CreateDepartment,UpdateDepartment

dep_router = APIRouter(prefix="/api/department",tags=["department"])

@dep_router.get("/{id}")
async def get_one(id:int,db:Session = Depends(get_db)):
    return department.get_one_department(db=db,dep_id=id)

@dep_router.get("/",response_model=List[Department])
async def get_one(db:Session = Depends(get_db)):
    return department.get_all_department(db=db)

@dep_router.post("/",response_model=Department)
async def create(dep: CreateDepartment,db:Session = Depends(get_db)):
    return department.create_department(db=db,dep=dep)

@dep_router.delete("/{id}",response_model=None)
async def delete(id:int,db:Session = Depends(get_db)):
    return department.delete_member(db=db,id=id)

@dep_router.patch("/{id}",response_model=Department)
async def update(id:int,value:UpdateDepartment,db:Session = Depends(get_db)):
    return department.update_member(db=db,id=id,value=value)