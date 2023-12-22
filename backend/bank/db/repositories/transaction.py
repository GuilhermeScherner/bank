from typing import Any, Sequence

import sqlalchemy as sa
from sqlalchemy import Row

from bank.db.mappings.transaction import Transaction
from bank.db.repositories.base import BaseRepository


class TransactionRepository(BaseRepository[Transaction]):
    """Transaction repository."""

    def __init__(self, db: Any) -> None:
        super().__init__(db, Transaction)

    def get_all_account(self, account_id: int) -> Sequence[Row[Any]]:
        """
        Get all transactions from an account.

        :param account_id: account id.
        :return: Transaction
        """
        qb = sa.select(self.mapping).filter_by(account_id=account_id)
        return self.db.session.execute(qb).fetchall()
