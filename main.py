from fastapi import FastAPI

zekapi = FastAPI()

@zekapi.get('/main')
def index():
    return {"text":"Hello ZEK !"}

@zekapi.delete('/{id}')
def delete(id):
    return{"id":id}

@zekapi.get('/products/all') # IMPORTANT path conflict all like id thinking so should be before then '/products/{id}' get_product_by_id method
def get_all_product():
    return [{'id':1,'name':'Flybikes'},{'id':2,'name':'Federalbikes'}]   

@zekapi.get('/products/{id}')
def get_product_by_id(id: int): # id must be integer pydantic
    return {'id':id,'name':'Flybikes'}



