from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from app.app_statistic.repositories.statistic_repository import StatisticRepository
from app.database import get_session


class StatisticService:
    """
    Сервис для работы с информацией о Статистике.
    """

    def __init__(self, session: AsyncSession = Depends(get_session)):
        """
        Инициализация сервиса.

        :param session: Объект сессии для взаимодействия с базой данных.
        """

        self.session = session
        self.statistic_repository = StatisticRepository(session)

    async def get_statistics(self, **kwargs):
        """
        Получение всей статистики.
        :param kwargs: Параметры фильтрации запроса.
        :return:
        """

        return await self.statistic_repository.find_all(**kwargs)
