from fastapi import Depends, HTTPException,status
from fastapi.routing import APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from auth import oauth2
from db.database import get_db
from db.models import DbUser
from db.hash import Hash
router = APIRouter(
    tags=['authentication']
)

@router.post('/token')
def get_token(request:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db) ):
    user = db.query(DbUser).filter(DbUser.username == request.username).first()

    if user and Hash.verify(user.password,request.password):
        access_token = oauth2.create_access_token(data={'sub':user.username})

        return {
            'access_token':access_token,
            'token_type':'bearer',
            'user_id':user.id,
            'user_name':user.username
        }
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect username or password !")