"""匹配度评分与过敏源匹配（核心业务规则）

规则见 README「业务规则」：
- 基础 100 分；命中过敏源扣 50 分；不符合饮食偏好每项扣 10 分
- 90-100 非常适合 / 70-89 比较适合 / 50-69 一般 / 0-49 不适合
"""
from sqlmodel import Session, select

from app.models.user import Allergen, DietPreference, UserAllergen, UserDiet


def load_user_allergens(session: Session, user_id: int) -> list[dict]:
    rows = session.exec(
        select(Allergen)
        .join(UserAllergen, UserAllergen.allergen_id == Allergen.id)
        .where(UserAllergen.user_id == user_id)
    ).all()
    return [{"name": a.name, "keywords": a.keywords or []} for a in rows]


def load_user_diets(session: Session, user_id: int) -> list[dict]:
    rows = session.exec(
        select(DietPreference)
        .join(UserDiet, UserDiet.diet_id == DietPreference.id)
        .where(UserDiet.user_id == user_id)
    ).all()
    return [{"name": d.name, "keywords": d.keywords or []} for d in rows]


def match_allergens(ingredients: list[str], user_allergens: list[dict]) -> list[dict]:
    """关键词匹配：命中返回 [{allergen_name, ingredient}]"""
    hits: list[dict] = []
    for ing in ingredients:
        for allergen in user_allergens:
            if any(kw in ing for kw in allergen["keywords"]):
                hits.append({"allergen_name": allergen["name"], "ingredient": ing})
    return hits


def violates_diet(ingredients: list[str], tags: list[str], diet: dict) -> bool:
    """简单关键词判断：商品标签明确符合偏好（如“低糖”）视为不违规"""
    if diet["name"] in tags:
        return False
    return any(kw in ing for ing in ingredients for kw in diet["keywords"])


def score_level(score: int) -> str:
    if score >= 90:
        return "非常适合"
    if score >= 70:
        return "比较适合"
    if score >= 50:
        return "一般"
    return "不适合"


def analyze_product(product: dict, user_allergens: list[dict], user_diets: list[dict]) -> dict:
    ingredients = product.get("ingredients", [])
    tags = product.get("tags", [])

    hits = match_allergens(ingredients, user_allergens)
    score = 100
    if hits:
        score -= 50
    for diet in user_diets:
        if violates_diet(ingredients, tags, diet):
            score -= 10
    score = max(0, score)

    return {
        "score": score,
        "level": score_level(score),
        "allergen_hits": hits,
        "recommended": (not hits) and score >= 50,
    }
