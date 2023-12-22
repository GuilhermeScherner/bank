from typing import Any, Dict

from bank.db.mappings.base import BaseMapping, db


class Account(BaseMapping):
    """Account Mapping."""

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship(
        "User",
        back_populates="account",
        uselist=False,
        primaryjoin="Account.user_id == User.id",
    )
    transaction = db.relationship(
        "Transaction",
        back_populates="account",
        primaryjoin="Account.id == Transaction.account_id",
    )
    balance = db.Column(db.Float, default=0)
    daily_withdrawal_limit = db.Column(db.Float, default=1000.0)
    is_active = db.Column(db.Boolean, default=True)
    account_type = db.Column(db.Integer)

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
            "daily_withdrawal_limit": self.daily_withdrawal_limit,
            "is_active": self.is_active,
            "account_type": self.account_type,
            "created_at": self.created_at,
        }
