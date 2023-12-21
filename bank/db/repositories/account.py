from typing import Any, Optional

import sqlalchemy as sa

from bank.db.mappings.account import Account
from bank.db.repositories.base import BaseRepository


class AccountRepository(BaseRepository[Account]):
    """Account repository."""

    def __init__(self, db: Any) -> None:
        super().__init__(db, Account)

    def get_by_user_id(self, user_id: int) -> Optional[Account]:
        """
        Get an account by user id.

        :param user_id: User id
        :return: Account
        """
        qb = sa.select(Account).where(Account.user_id == user_id)
        return self.db.session.execute(qb).scalar_one_or_none()
