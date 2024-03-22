from datetime import datetime

from typing_extensions import Annotated

from sqlalchemy.orm import mapped_column


int_pk = Annotated[int, mapped_column(primary_key=True)]

timestamp = Annotated[
    datetime,
    mapped_column(nullable=False, default=datetime.utcnow),
]