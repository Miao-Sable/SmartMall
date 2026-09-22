"""商品相关模型"""
from pydantic import BaseModel


class NutritionItem(BaseModel):
    name: str
    value: str
    unit: str
    per: str = "100g"


class ProductOut(BaseModel):
    id: int
    barcode: str
    name: str
    brand: str = ""
    category: str = ""
    image_url: str = ""
    description: str = ""
    ingredients: list[str] = []
    tags: list[str] = []
    nutrition: list[NutritionItem] = []


class PricePoint(BaseModel):
    date: str
    price: float


class PriceHistoryOut(BaseModel):
    product_id: int
    barcode: str = ""
    points: list[PricePoint] = []
