from src.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Member(Base):
    __tablename__ = "member"

    id = Column("id", Integer, autoincrement=True, primary_key=True)
    name = Column( "name", String(16), nullable=False)
    age = Column( "age", Integer,nullable=False)
    dep_id = Column("dep_id",Integer,ForeignKey("department.dep_id"),nullable=False)

    class Config:
        orm_mode = True