from sqlalchemy.ext.asyncio import AsyncSession

from bank.db.mappings.user import User
from bank.db.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    """User repository."""

    def __init__(self, db: AsyncSession) -> None:
        super().__init__(db, User)
