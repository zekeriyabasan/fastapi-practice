from typing import List, Optional
from fastapi import APIRouter, Query
from models.product_model import Product


router = APIRouter(
    prefix='/products',
    tags=['products']
)


@router.delete('/{id}')
def delete(id: int, v:Optional[List[str]] = Query(None)): # optinal list str parameters
    return{"id":id, "values": v}

@router.delete('/')
def delete(v:Optional[List[str]] = Query(['default 1','default 2','default 3'], title="delete products by Id", description= "you should enter the id of product for delete")): # optinal list str parameters with defaults
    return{"values": v}