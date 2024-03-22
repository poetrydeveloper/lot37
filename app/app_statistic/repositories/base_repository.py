from abc import ABC, abstractmethod
from typing import Type, Sequence

from pydantic import BaseModel
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository(ABC):
    """
    Базовый абстрактный класс репозитория.
    """

    def __init__(self, session: AsyncSession) -> None:
        """
        Инициализация репозитория.

        :param session: Объект сессии для взаимодействия с БД
        """

        self.session = session

    @property
    @abstractmethod
    def model(self) -> Type[BaseModel]:
        """
        Модель таблицы.
        """

    async def find_all(self, **kwargs) -> Sequence[BaseModel]:
        """
        Вернуть все объекты по заданным фильтрам.

        :param kwargs: Словарь для фильтрации запроса.
        :return:
        """

        query = select(self.model).filter_by(**kwargs)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create(self, **kwargs) -> BaseModel:
        """
        Создать объект.

        :param kwargs: Данные для создания объекта модели.
        :return:
        """

        new_model = self.model(**kwargs)
        self.session.add(new_model)
        await self.session.commit()
        return new_model
