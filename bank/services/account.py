from typing import Any, Dict

from bank.services.base import BaseService
from bank.services.models import account as account_model


class AccountService(BaseService):
    """Account service."""

    async def balance(
        self,
        balance_model: account_model.BalanceRequest,
    ) -> Dict[str, Any]:
        """
        Get the balance of an account.

        :param balance_model: BalanceRequest
        :return: BalanceResponse
        """
        return {}

    async def change_state(
        self,
        change_state_model: account_model.ChangeStateRequest,
    ) -> Dict[str, Any]:
        """
        Change the state of an account.

        :param change_state_model: ChangeStateRequest
        :return: ChangeStateResponse
        """
        return {}

    async def orders(self, orders_model: account_model.OrdersRequest) -> Dict[str, Any]:
        """
        Get all orders from an account.

        :param orders_model: OrdersRequest
        :return: OrdersResponse
        """
        return {}
