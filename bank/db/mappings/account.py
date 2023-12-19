from typing import Any, Dict

from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from bank.db.mappings.base import BaseMapping


class Account(BaseMapping):
    """Account Mapping."""

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", backref="accounts")
    balance = Column(Float, default=0)
    daily_withdrawal_limit = Column(Float, default=1000.0)  # daily withdrawal
    is_active = Column(Boolean, default=True)
    account_type = Column(String(10), default="current")

    def __repr__(self) -> str:
        return f"<Account(user_id={self.user_id}, balance={self.balance})>"

    def to_dict(self) -> Dict[str, Any]:
        """
        A dict representation of the Account.

        :return: Account dict representation.
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "balance": self.balance,
        }
