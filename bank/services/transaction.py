from typing import Any, Dict

from bank.services.base import BaseService
from bank.services.models import transaction as transaction_model


class TransactionService(BaseService):
    """Control transactions operations."""

    async def deposit(
        self,
        deposit_model: transaction_model.DepositRequest,
    ) -> Dict[str, Any]:
        """
        Deposit money into an account.

        :param deposit_model: DepositRequest
        :return: DepositResponse
        """
        return {}

    async def withdraw(
        self,
        withdraw_model: transaction_model.WithdrawRequest,
    ) -> Dict[str, Any]:
        """
        Withdraw money from an account.

        :param withdraw_model: WithdrawRequest
        :return: WithdrawResponse
        """
        return {}
