"""数据库引擎与会话（SQLite 开发 / PostgreSQL 部署）"""
from sqlmodel import Session, SQLModel, create_engine

from app.core.config import settings

connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
engine = create_engine(settings.database_url, echo=settings.debug, connect_args=connect_args)


def get_session():
    """FastAPI 依赖：每个请求一个会话"""
    with Session(engine) as session:
        yield session


def init_db() -> None:
    """建表并初始化字典数据（幂等，可重复调用）"""
    # 导入模型模块，确保全部注册到 SQLModel.metadata
    from app import models  # noqa: F401
    from app.services.seed import seed_dicts

    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        seed_dicts(session)
