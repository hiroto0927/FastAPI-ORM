from src.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = "department"

    id = Column("dep_id" ,Integer,autoincrement=True, primary_key=True)
    name = Column("name",String,nullable=False)

    address = relationship("Member")

    class Config:
        orm_mode = True