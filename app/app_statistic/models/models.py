from app.app_statistic.models.mixin import TimestampMixin
from app.app_statistic.models.base import ABCBase

class Statistic(ABCBase, TimestampMixin):
    """
    Модель таблицы базы данных идей.
    """