from typing import Any, Dict, Generic, Optional, Type, TypeVar

import sqlalchemy as sa
from apiflask import Schema
from sqlalchemy.ext.asyncio import AsyncSession

from bank.db.mappings.base import BaseMapping

ModelType = TypeVar("ModelType", bound=Schema)
MappingType = TypeVar("MappingType", bound=BaseMapping)


class BaseRepository(Generic[MappingType]):
    """Base repository with common operations."""

    def __init__(self, db: AsyncSession, mapping: Type[MappingType]) -> None:
        self.mapping = mapping
        self.db = db

    async def add(self, obj: MappingType) -> MappingType:
        """
        Add an object to the database.

        :param obj: object to be added
        :return: added object
        """
        self.db.add(obj)
        await self.db.flush([obj])
        return obj

    async def get_by_id(self, mapping_id: int) -> Optional[MappingType]:
        """
        Get an object by its id.

        :param mapping_id: id of the object to be retrieved
        :return: Object or None
        """
        qb = sa.select(self.mapping).where(self.mapping.id == mapping_id)
        result = await self.db.execute(qb)
        return result.scalars().first()

    async def update_by_id(
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
        await self.db.execute(qb)
        return await self.get_by_id(mapping_id)
