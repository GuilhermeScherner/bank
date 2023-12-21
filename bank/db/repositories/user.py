from typing import Optional

import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy

from bank.db.mappings.user import User
from bank.db.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    """User repository."""

    def __init__(self, db: SQLAlchemy) -> None:
        super().__init__(db, User)

    def get_by_username(self, username: str) -> Optional[User]:
        """
        Return a user by username.

        :param username: User username.
        :return: User.
        """
        qb = sa.select(User).where(User.username == username)
        return self.db.session.execute(qb).scalar_one_or_none()
