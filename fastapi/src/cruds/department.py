from sqlalchemy.orm import Session
from src.models.department import Department
from src.schema.department import CreateDepartment,UpdateDepartment

def get_one_department(db:Session,dep_id:int):
    return db.query(Department).filter(Department.id==dep_id).first()

def get_all_department(db:Session):
    return db.query(Department).all()

def create_department(db:Session, dep:CreateDepartment):
    query = Department(name=dep.name)
    db.add(query)
    db.commit()

    return query

def update_member(db: Session, id: int, value: UpdateDepartment):

    query = db.query(Department).filter(Department.id==id)
    query.update(value.dict(exclude_unset=True))

    db.commit()

    return query.first()

def delete_member(db: Session, id: int):

    db.query(Department).filter(Department.id == id).delete()

    db.commit()

    return