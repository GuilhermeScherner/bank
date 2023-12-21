from typing import Any, Dict

import jwt
from apiflask import HTTPError, HTTPTokenAuth

from bank.constants import UNAUTHORIZED
from bank.db.database import RepositoryFactory
from bank.services.account import AccountService
from bank.services.transaction import TransactionService
from bank.services.user import UserService
from bank.settings import settings

auth = HTTPTokenAuth(scheme="Bearer")


def user_service_dependency() -> UserService:
    """
    Get the user service.

    :return: UserService
    """
    repo: RepositoryFactory = RepositoryFactory()
    return UserService(repo)


def transaction_service_dependency() -> TransactionService:
    """
    Get the transaction service.

    :return: TransactionService
    """
    repo: RepositoryFactory = RepositoryFactory()
    return TransactionService(repo)


def account_service_dependency() -> AccountService:
    """
    Get the account service.

    :return: AccountService
    """
    repo: RepositoryFactory = RepositoryFactory()
    return AccountService(repo)


@auth.verify_token
def extract_user_data(token: str) -> Dict[str, Any]:
    """
    Extract user data from the token.

    :param token: Token
    :return: User data
    :raises HTTPError: Invalid token
    """
    try:
        payload = jwt.decode(token, settings.bank_secret_key, algorithms=["HS256"])

        return {
            "id": payload.get("user_id"),
            "username": payload.get("username"),
        }
    except jwt.exceptions.DecodeError:
        raise HTTPError(
            UNAUTHORIZED["code"],
            message=UNAUTHORIZED["message"].format("Token"),
        )
