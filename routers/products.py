from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/api" , tags=['Products'])

class Products(BaseModel):
    title: str
    price: float
    category: str
    description: str
    image: str | None = None



@router.get("/products")
async def get_all_products(products: Products):
    return products