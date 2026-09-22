"""首页仪表板统计模型"""
from pydantic import BaseModel


class DailyCount(BaseModel):
    date: str
    count: int


class StatsOverview(BaseModel):
    total_scans: int = 0
    allergen_alerts: int = 0
    today_scans: int = 0
    avg_score: float = 0
    recent_days: list[DailyCount] = []
