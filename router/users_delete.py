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


# Delete User

@router.delete('/{id}')
def delete_user(id:int, response:Response, db:Session = Depends(get_db)):
    db_user.delete_user(db, id)
    response.status_code = status.HTTP_204_NO_CONTENT


