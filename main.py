from enum import Enum
from typing import Optional
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

class ProductType(str, Enum):
    techno = "technology"
    energy = "energy"
    drink = "drink"
    car = "car"

@zekapi.get('/products/type/{type}')
def get_product_by_type(type: ProductType):
    return {'id':2, 'name':f"Product {type}", 'type':type}

@zekapi.get('/products/{id}/filter/{type}')
def get_product_by_filter(id:int, type: ProductType, name:str, max_price:Optional[float], min_price:float = 0): # default par must be last parameter
    return {'message':f"your data has id {id} - type {type} - name {name} min_price {min_price} - max_price {max_price}"}



