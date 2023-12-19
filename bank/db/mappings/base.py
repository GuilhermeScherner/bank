import re

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import declarative_mixin
from sqlalchemy.sql import func


def camel_to_snake(name: str):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


@declarative_mixin
class TimestampedMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


@declarative_mixin
class TableNameMixin:
    @declared_attr
    def __tablename__(cls) -> str:  # noqa: N805
        return camel_to_snake(cls.__name__)


@declarative_mixin
class UUIDMixin:
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
    )


@as_declarative()
class BaseMapping(TimestampedMixin, TableNameMixin, UUIDMixin):
    pass
