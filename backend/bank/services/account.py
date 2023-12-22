from typing import Any, Dict

from apiflask.fields import Integer

from bank.services.base import BaseService
from bank.services.models import account as account_model


class AccountService(BaseService):
    """Account service."""

    def balance(
        self,
        user_id: int | Integer,
    ) -> Dict[str, Any]:
        """
        Get the balance of an account.

        :param user_id: user id
        :return: BalanceResponse
        """
        result = self._validate_account(user_id)
        return result.to_dict()

    def change_state(
        self,
        change_state_request: account_model.ChangeStateRequest,
    ) -> Dict[str, Any]:
        """
        Change the state of an account.

        :param change_state_request: ChangeStateRequest
        :return: ChangeStateResponse
        """
        account = self._validate_account(change_state_request.user_id)

        self.repo.account.update_by_id(
            account.id,
            {"is_active": change_state_request.state},
        )

        return account.to_dict()
