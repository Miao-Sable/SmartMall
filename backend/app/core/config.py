"""应用配置（通过环境变量 / .env 覆盖默认值）"""
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# 项目根目录（backend/ 的上一级）
PROJECT_ROOT = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "智慧购物 API"
    debug: bool = True

    # 生产环境务必通过环境变量覆盖！
    secret_key: str = "dev-secret-key-change-me"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24 * 7

    # SQLite 开发 / PostgreSQL 部署（如 postgresql://user:pass@host/db）
    database_url: str = f"sqlite:///{PROJECT_ROOT / 'smartmall.db'}"

    # mock 数据目录
    mock_dir: Path = PROJECT_ROOT / "mock"

    cors_origins: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]


settings = Settings()
