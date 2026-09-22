"""基础字典：过敏源 / 饮食偏好"""
from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.database import get_session
from app.models.user import Allergen, DietPreference
from app.schemas.meta import AllergenOut, DietOut

router = APIRouter()


@router.get("/allergens", response_model=list[AllergenOut])
def list_allergens(session: Session = Depends(get_session)) -> list[Allergen]:
    return session.exec(select(Allergen).order_by(Allergen.id)).all()


@router.get("/diet-preferences", response_model=list[DietOut])
def list_diet_preferences(session: Session = Depends(get_session)) -> list[DietPreference]:
    return session.exec(select(DietPreference).order_by(DietPreference.id)).all()
