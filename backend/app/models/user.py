"""用户相关表：账号、档案、过敏源/饮食偏好字典与关联"""
from datetime import datetime, timezone

from sqlalchemy import JSON, Column
from sqlmodel import Field, SQLModel


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class User(SQLModel, table=True):
    __tablename__ = "user"

    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    phone: str | None = Field(default=None, index=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=utcnow)


class UserProfile(SQLModel, table=True):
    __tablename__ = "user_profile"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", unique=True)
    nickname: str = ""
    gender: str = ""  # male / female / other
    birth_year: int | None = None
    updated_at: datetime = Field(default_factory=utcnow)


class Allergen(SQLModel, table=True):
    __tablename__ = "allergen"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)
    category: str = ""
    keywords: list = Field(default_factory=list, sa_column=Column(JSON))  # 关键词列表
    description: str = ""


class UserAllergen(SQLModel, table=True):
    __tablename__ = "user_allergen"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    allergen_id: int = Field(foreign_key="allergen.id")


class DietPreference(SQLModel, table=True):
    __tablename__ = "diet_preference"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)
    keywords: list = Field(default_factory=list, sa_column=Column(JSON))
    description: str = ""


class UserDiet(SQLModel, table=True):
    __tablename__ = "user_diet"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    diet_id: int = Field(foreign_key="diet_preference.id")
