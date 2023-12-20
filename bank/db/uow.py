from __future__ import annotations

from functools import cached_property
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from bank.db.repositories.user import UserRepository


class UnitOfWork:
    """Unit of work."""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def __aenter__(self) -> UnitOfWork:
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if exc_type:
            await self.rollback()
        else:
            await self.commit()

    async def commit(self) -> None:
        """Commit the session."""
        await self.session.commit()

    async def rollback(self) -> None:
        """Rollback the session."""
        await self.session.rollback()

    @cached_property
    def user(self) -> UserRepository:
        """
        User repository.

        :return: UserRepository
        """
        return UserRepository(self.session)
