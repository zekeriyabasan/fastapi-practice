from dataclasses import dataclass
from enum import Enum
from typing import Optional
from fastapi import FastAPI, Response
from starlette import status

zekapi = FastAPI()

@zekapi.get('/main', tags=['main'])
def index():
    return {"text":"Hello ZEK !"}

@zekapi.delete('/{id}', tags=['product-remove'])
def delete(id):
    return{"id":id}

@zekapi.get('/products/all', tags=['product']) # IMPORTANT path conflict all like id thinking so should be before then '/products/{id}' get_product_by_id method
def get_all_product():
    return [{'id':1,'name':'Flybikes'},{'id':2,'name':'Federalbikes'}]   

@zekapi.get('/products/{id}', tags=['product'])
def get_product_by_id(id: int): # id must be integer pydantic
    return {'id':id,'name':'Flybikes'}

class ProductType(str, Enum):
    techno = "technology"
    energy = "energy"
    drink = "drink"
    car = "car"

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int

@zekapi.get('/products/type/{type}', tags=['product', 'product-type'])
def get_product_by_type(type: ProductType):
    return {'id':2, 'name':f"Product {type}", 'type':type}

@zekapi.get('/products/{id}/filter/{type}', tags=['product','product-type'])
def get_product_by_filter(id:int, type: ProductType, name:str, max_price:Optional[float], min_price:float = 0): # default par must be last parameter
    return {'message':f"your data has id {id} - type {type} - name {name} min_price {min_price} - max_price {max_price}"}

@zekapi.post('/products', tags=['product'])
def create_a_product(product:Product, response:Response):
    response.status_code = status.HTTP_201_CREATED
    return {'product':product}

@zekapi.put('/products/{id}', tags=['product'])
def update_a_product(id:int, product:Product, response:Response):
    if(id > 10) :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message':f'not found product {product}'}
    
    response.status_code = status.HTTP_204_NO_CONTENT



