"""商品相关表。

MVP 阶段商品数据来自本地 mock JSON（见 services/mock_data.py），
以下表为后续接入真实商品数据源预留，当前不参与业务读写。
"""
from datetime import datetime, timezone


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):
    __tablename__ = "product"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    brand: str = ""
    category: str = ""
    image_url: str = ""
    description: str = ""
    tags: str = ""  # 逗号分隔，如 "低糖,素食"
    created_at: datetime = Field(default_factory=utcnow)


class ProductBarcode(SQLModel, table=True):
    __tablename__ = "product_barcode"

    id: int | None = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id", index=True)
    barcode: str = Field(unique=True, index=True)


class ProductIngredient(SQLModel, table=True):
    __tablename__ = "product_ingredient"

    id: int | None = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id", index=True)
    name: str
    is_allergen: bool = False


class ProductNutrition(SQLModel, table=True):
    __tablename__ = "product_nutrition"

    id: int | None = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id", index=True)
    name: str
    value: str = ""
    unit: str = ""
    per: str = "100g"


class PriceHistory(SQLModel, table=True):
    __tablename__ = "price_history"

    id: int | None = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id", index=True)
    price: float
    currency: str = "CNY"
    source: str = "mock"
    recorded_at: datetime = Field(default_factory=utcnow)


class KeywordLibrary(SQLModel, table=True):
    """过敏源关键词库（与 allergen.keywords 互补，后续做模糊匹配）"""
    __tablename__ = "keyword_library"

    id: int | None = Field(default=None, primary_key=True)
    keyword: str = Field(unique=True, index=True)
    allergen_id: int | None = Field(default=None, foreign_key="allergen.id")
