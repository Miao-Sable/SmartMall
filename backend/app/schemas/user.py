"""用户档案相关模型"""
from pydantic import BaseModel


class UserProfileOut(BaseModel):
    user_id: int
    email: str
    nickname: str = ""
    gender: str = ""
    birth_year: int | None = None
    allergen_ids: list[int] = []
    diet_ids: list[int] = []
    onboarded: bool = False


class UserProfileUpdate(BaseModel):
    nickname: str = ""
    gender: str = ""
    birth_year: int | None = None
    allergen_ids: list[int] = []
    diet_ids: list[int] = []
