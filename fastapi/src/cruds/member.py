from sqlalchemy.orm import Session
from src.models.member import Member
from src.schema.member import CreateMember,UpdateMember

def get_one_member(db:Session,id:int):
    return db.query(Member).filter(Member.id==id).first()

def get_all_member(db:Session):
    return db.query(Member).all()

def create_member(db:Session, member:CreateMember):
    query = Member(name=member.name,age=member.age, dep_id=member.dep_id)
    db.add(query)
    db.commit()

    return query

def update_member(db: Session, id: int, value: UpdateMember):

    query = db.query(Member).filter(Member.id==id)
    query.update(value.dict(exclude_unset=True))

    db.commit()

    return query.first()

# delete
def delete_member(db: Session, id: int):

    db.query(Member).filter(Member.id == id).delete()

    db.commit()

    return