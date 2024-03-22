from app.app_statistic.models.mixin import TimestampMixin
from app.app_statistic.models.base import ABCBase
from sqlalchemy.orm import Mapped, mapped_column
from app.app_statistic.models.enum import DepartmentsEnum


class Statistic(ABCBase, TimestampMixin):
    """
    Модель таблицы базы данных Статистики.
    """

    __tablename__ = 'statistic'

    id = Mapped[int]
    department: Mapped[DepartmentsEnum] = mapped_column(default=DepartmentsEnum.MARKETING)
    mass: Mapped[int]
    personal: Mapped[int]
    informational: Mapped[int]
    survey: Mapped[int]
    commercial_survey: Mapped[int]
    service: Mapped[int]
