from typing import Any, Dict

from apiflask.fields import Integer

from bank.db.mappings.transaction import Transaction
from bank.services.base import BaseService


class TransactionService(BaseService):
    """Control transactions operations."""

    def deposit(
        self,
        deposit_model: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Deposit money into an account.

        :param deposit_model: DepositRequest
        :return: DepositResponse
        """
        account = self._validate_account(deposit_model["user_id"])
        self.repo.account.update_by_id(
            account.id,
            {"balance": account.balance + deposit_model["amount"]},
        )
        transaction = Transaction(
            account_id=account.id,
            amount=deposit_model["amount"],
        )
        result = self.repo.transaction.add(
            transaction,
        )

        return {"transaction_id": result.id}

    def withdraw(
        self,
        withdraw_model: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Withdraw money from an account.

        :param withdraw_model: WithdrawRequest
        :return: WithdrawResponse
        """
        account = self._validate_account(withdraw_model["user_id"])
        self.repo.account.update_by_id(
            account.id,
            {"balance": account.balance - withdraw_model["amount"]},
        )
        transaction = Transaction(
            account_id=account.id,
            amount=-withdraw_model["amount"],
        )
        result = self.repo.transaction.add(
            transaction,
        )

        return {"transaction_id": result.id}

    def orders(self, user_id: int | Integer) -> Dict[str, Any]:
        """
        Get all orders from an account.

        :param user_id: user id.
        :return: OrdersResponse
        """
        account = self._validate_account(user_id)
        result = self.repo.transaction.get_all_account(account.id)
        response_list = [
            {"account_id": value[0].account_id, "amount": value[0].amount, "date": value[0].created_at}
            for value in result
        ]

        return {"data": response_list}
