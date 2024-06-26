from sqlalchemy.orm import Mapped

from app.database import Base
from app.app_statistic.models.types import int_pk


class ABCBase(Base):
    """
    Базовый класс для всех моделей.
    """
    __abstract__ = True

    id: Mapped[int_pk]