
from fastapi.security import OAuth2PasswordBearer

oauth2_schemas = OAuth2PasswordBearer(tokenUrl="token") # bu şema ile token göndermek zorunda kalıyor