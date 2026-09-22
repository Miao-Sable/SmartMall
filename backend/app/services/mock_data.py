"""MVP 商品数据：从本地 mock JSON 读取。

后续接入真实商品 API（阿里云、聚合数据等）时，替换本模块实现即可，
routers 层无需改动。
"""
import json
from functools import lru_cache

from app.core.config import settings


@lru_cache(maxsize=None)
def _load(name: str) -> list:
    with open(settings.mock_dir / name, encoding="utf-8") as f:
        return json.load(f)


def find_product_by_barcode(barcode: str) -> dict | None:
    for product in _load("products.json"):
        if str(product.get("barcode")) == str(barcode):
            return product
    return None


def load_price_history(product_id: int) -> dict | None:
    for item in _load("price_history.json"):
        if item.get("product_id") == product_id:
            return item
    return None


def load_allergens() -> list:
    return _load("allergens.json")


def load_diet_preferences() -> list:
    return _load("diet_preferences.json")
