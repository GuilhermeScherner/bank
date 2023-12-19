from typing import Any, Dict

from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from bank.db.mappings.base import BaseMapping


class Transaction(BaseMapping):
    """Transaction Mapping."""

    account_id = Column(Integer, ForeignKey("account.id"))
    account = relationship("Account", backref="transactions")
    amount = Column(Float, default=0)

    def __repr__(self) -> str:
        return f"<Transaction(account_id={self.account_id}, amount={self.amount})>"

    def to_dict(self) -> Dict[str, Any]:
        """
        Return a dict representation of the Transaction.

        :return: Transaction dict representation.
        """
        return {
            "id": self.id,
            "account_id": self.account_id,
            "amount": self.amount,
            "transaction_date": self.created_at,
        }
