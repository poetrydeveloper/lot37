from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from config import settings

"""Настройки, подключения к базе данных"""


engine = create_async_engine(settings.database_url)


async def get_session() -> AsyncSession:
    """
    Получение объекта сессии для асинхронного подключения к БД.

    :return:
    """

    async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session


class Base(DeclarativeBase):
    pass
