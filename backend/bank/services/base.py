from typing import cast

from apiflask import HTTPError
from apiflask.fields import Integer

from bank.constants import NOT_FOUND
from bank.db.database import RepositoryFactory
from bank.db.mappings.account import Account


class BaseService:
    """Base service."""

    def __init__(self, repo: RepositoryFactory) -> None:
        """
        Constructor.

        :param repo: RepositoryFactory
        """
        self.repo = repo

    def _validate_account(self, user_id: Integer | int) -> Account:
        """
        Validate if an account exists.

        :param user_id: user id
        :return: Account
        :raises HTTPError: Account not found
        """
        result = self.repo.account.get_by_user_id(cast(int, user_id))

        if not result or result.is_active is False:
            raise HTTPError(
                NOT_FOUND["code"],
                message=NOT_FOUND["message"].format("Account"),
            )
        return result
