from typing import Any, Dict, Generic, Optional, Type, TypeVar

import sqlalchemy as sa
from apiflask import Schema
from flask_sqlalchemy import SQLAlchemy

from bank.db.mappings.base import BaseMapping

ModelType = TypeVar("ModelType", bound=Schema)
MappingType = TypeVar("MappingType", bound=BaseMapping)


class BaseRepository(Generic[MappingType]):
    """Base repository with common operations."""

    def __init__(self, db: SQLAlchemy, mapping: Type[MappingType]) -> None:
        self.mapping = mapping
        self.db = db

    def add(self, obj: MappingType) -> MappingType:
        """
        Add an object to the database.

        :param obj: object to be added
        :return: added object
        """
        self.db.session.add(obj)
        self.db.session.flush([obj])
        self.db.session.commit()
        return obj

    def get_by_id(self, mapping_id: int) -> Optional[MappingType]:
        """
        Get an object by its id.

        :param mapping_id: id of the object to be retrieved
        :return: Object or None
        """
        qb = sa.select(self.mapping).where(self.mapping.id == mapping_id)
        result = self.db.session.execute(qb)
        return result.scalars().first()

    def update_by_id(
        self,
        mapping_id: int,
        batch: Dict[str, Any],
    ) -> Optional[MappingType]:
        """
        Update an object by its id.

        :param mapping_id: id of the object to be updated
        :param batch: batch of fields to be updated
        :return: updated object
        """
        qb = (
            sa.update(self.mapping)
            .where(self.mapping.id == str(mapping_id))
            .values(batch)
        )
        self.db.session.execute(qb)
        self.db.session.commit()
        return self.get_by_id(mapping_id)

    def get_all(self) -> Optional[MappingType]:
        """
        Get all objects.

        :return: all objects
        """
        qb = sa.select(self.mapping)
        result = self.db.execute(qb)
        return result.scalars().all()
