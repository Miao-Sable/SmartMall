"""初始化字典数据：从 mock JSON 灌入 allergen / diet_preference 表（幂等）"""
from sqlmodel import Session, select

from app.models.user import Allergen, DietPreference
from app.services.mock_data import load_allergens, load_diet_preferences


def seed_dicts(session: Session) -> None:
    if session.exec(select(Allergen)).first() is None:
        for item in load_allergens():
            session.add(
                Allergen(
                    name=item["name"],
                    category=item.get("category", ""),
                    keywords=item.get("keywords", []),
                    description=item.get("description", ""),
                )
            )

    if session.exec(select(DietPreference)).first() is None:
        for item in load_diet_preferences():
            session.add(
                DietPreference(
                    name=item["name"],
                    keywords=item.get("keywords", []),
                    description=item.get("description", ""),
                )
            )

    session.commit()
