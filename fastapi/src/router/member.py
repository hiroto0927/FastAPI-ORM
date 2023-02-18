from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from src.cruds import member
from typing import List
from src.db.database import get_db
from src.schema.member import Member
from src.schema.member import CreateMember,UpdateMember

member_router = APIRouter(prefix="/api/member",tags=["member"])

@member_router.get("/{id}",response_model=Member)
async def get_one(id:int,db:Session = Depends(get_db)):
    return member.get_one_member(db=db,id=id)

@member_router.get("/",response_model=List[Member])
async def get_one(db:Session = Depends(get_db)):
    return member.get_all_member(db=db)

@member_router.post("/",response_model=Member)
async def create(value:CreateMember,db:Session = Depends(get_db)):
    return member.create_member(db=db,member=value)

@member_router.delete("/{id}",response_model=None)
async def delete(id:int,db:Session = Depends(get_db)):
    return member.delete_member(db=db,id=id)

@member_router.patch("/{id}",response_model=Member)
async def update(id:int,value:UpdateMember,db:Session = Depends(get_db)):
    return member.update_member(db=db,id=id,value=value)