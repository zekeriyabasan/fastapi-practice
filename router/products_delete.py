from typing import List, Optional
from fastapi import APIRouter, Path, Query
from models.product_model import Product


router = APIRouter(
    prefix='/products',
    tags=['products']
)


@router.delete('/{id}')
def delete(id: int = Path(..., gt = 0, le=100), v:Optional[List[str]] = Query(None)): # optional list str parameters --- Path prameters 0 <id <= 100
    return{"id":id, "values": v}

@router.delete('/')
def delete(v:Optional[List[str]] = Query(['default 1','default 2','default 3'], title="delete products by Id", description= "you should enter the id of product for delete")): # optinal list str parameters with defaults
    return{"values": v}
