from typing import Type
from app.app_statistic.models.models import Statistic
from app.app_statistic.repositories.base_repository import BaseRepository


class StatisticRepository(BaseRepository):
    """
    Репозиторий для Статистики.
    """

    @property
    def model(self) -> Type[Statistic]:
        return Statistic
