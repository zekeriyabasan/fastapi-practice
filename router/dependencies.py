from fastapi import APIRouter, Depends, Request

router = APIRouter(
    prefix='/dependencies',
    tags=['dependencies']
)

def convert_queries(request:Request, seperator:str):
    out_queries = []
    for key,value in request.query_params.items():
        out_queries.append(f"{key}{seperator}{value}")

    return out_queries

def convert_headers(request:Request, seperator:str = "--", out_queries = Depends(convert_queries)):
    out_headers = []
    for key,value in request.headers.items():
        out_headers.append(f"{key}{seperator}{value}")

    return {
        "out_headers":out_headers,
        "out_queries":out_queries
    }

@router.get('/')
def get_items(headers = Depends(convert_headers)): # not have a seperator params but I send this params because depends function has this params
    return{
        "items":["a","b","c"],
        "headers":headers
    }

@router.post('/')
def get_items(seperator:str="--",headers = Depends(convert_headers)): # sperator own parameter but used the Depends function
    return{
        "items":["a","b","c"],
        "headers":headers
    }

class Account:
    def __init__(self,name, email, surname):
        self.name = name
        self.email = email
        self.fullname = name + " " + surname

@router.post('/user')
def create_account(name:str, email:str, password:str, account:Account = Depends(Account)):
    #account - perform whatever operations
    return{
        "name": account.name,
        "email":account.email,
        "fullname":account.fullname
    }

@router.get('/multi-depends')
def get_items_multi_depends(name:str, zek:str, seperator:str="--", headers = Depends(convert_headers)): # not have a seperator params but I send this params because depends function has this params
    return{
        "items":["a","b","c"],
        "headers":headers
    }