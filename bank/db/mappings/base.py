import re

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import declarative_mixin
from sqlalchemy.sql import func
from sqlalchemy.util import classproperty


def camel_to_snake(name: str) -> str:
    """
    Convert CamelCase to snake_case.

    :param name: CamelCase string.
    :return: snake_case string.
    """
    return re.sub("(?<!^)(?=[A-Z])", "_", name).lower()


@declarative_mixin
class TimestampedMixin:
    """Generate times Created and Updated."""

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


@declarative_mixin
class TableNameMixin:
    """Generate Table Name."""

    @classproperty
    def __tablename__(cls) -> str:  # noqa: N805
        return camel_to_snake(cls.__name__)  # type: ignore


@declarative_mixin
class IDMixin:
    """Generate ID."""

    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
    )


@as_declarative()
class BaseMapping(TimestampedMixin, TableNameMixin, IDMixin):
    """Base Mapping for all class."""
