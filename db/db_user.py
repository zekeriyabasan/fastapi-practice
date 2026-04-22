from sqlalchemy.orm.session import Session

from db.hash import Hash
from db.models import DbUser
from db.schemas import UserBase

# Create User

def create_user(db:Session, request:UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Read User

def get_all_user(db:Session):
    return db.query(DbUser).all()

def get_user(db:Session, id: int):
    return db.query(DbUser).filter(DbUser.id == id).first()

# Update User

def update_user(db:Session, id:int, request:UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username : request.username,
        DbUser.email : request.email,
        DbUser.password : Hash.bcrypt(request.password)
    })
    db.commit()
    return "ok"

# Delete User

def delete_user(db:Session, id:int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    db.delete(user)
    db.commit()


