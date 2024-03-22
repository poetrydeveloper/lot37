from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from app.app_statistic.models.types import timestamp


class TimestampMixin:
    """
    Миксин для добавления атрибутов с датой и временем создания и обновления записи.
    """
    created_at: Mapped[timestamp]
    updated_at: Mapped[timestamp] = mapped_column(onupdate=datetime.utcnow)
