from functools import cached_property

from bank.db.mappings.base import db
from bank.db.repositories.account import AccountRepository
from bank.db.repositories.transaction import TransactionRepository
from bank.db.repositories.user import UserRepository


class RepositoryFactory:
    """Repository factory."""

    def __init__(self) -> None:
        self.db = db

    async def __aenter__(self) -> "RepositoryFactory":
        return self

    @cached_property
    def account(self) -> AccountRepository:
        """
        Return a AccountRepository instance.

        :return: AccountRepository instance.
        """
        return AccountRepository(self.db)

    @cached_property
    def transaction(self) -> TransactionRepository:
        """
        Return a TransactionRepository instance.

        :return: TransactionRepository instance.
        """
        return TransactionRepository(self.db)

    @cached_property
    def user(self) -> UserRepository:
        """
        Return a UserRepository instance.

        :return: UserRepository instance.
        """
        return UserRepository(self.db)


def get_repository_factory() -> RepositoryFactory:
    """
    Return a RepositoryFactory instance.

    :return: RepositoryFactory instance.
    """
    return RepositoryFactory()
