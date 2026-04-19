from fastapi import APIRouter, Depends, Response
from starlette import status
from sqlalchemy.orm.session import Session
from db import db_user
from db.database import get_db
from db.schemas import UserBase


router = APIRouter(
    prefix='/users',
    tags=['users']
)


# Update User

@router.put('/{id}')
def update_user(id:int, request:UserBase, response:Response, db:Session = Depends(get_db)):
    result = db_user.update_user(db, id, request)
    response.status_code = status.HTTP_200_OK
    return result

