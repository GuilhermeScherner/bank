from typing import Any, Dict

from bank.db.mappings.base import BaseMapping, db


class Transaction(BaseMapping):
    """Transaction Mapping."""

    account_id = db.Column(db.Integer, db.ForeignKey("account.id"))
    account = db.relationship(
        "Account",
        back_populates="transaction",
        primaryjoin="Transaction.account_id == Account.id",
    )
    amount = db.Column(db.Float, default=0)

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
