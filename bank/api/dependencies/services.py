from typing import Any

from flask_httpauth import HTTPBasicAuth
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.pool import NullPool

from bank.db.uow import UnitOfWork
from bank.services.account import AccountService
from bank.services.transaction import TransactionService
from bank.services.user import UserService

engine = create_async_engine("database_url", poolclass=NullPool)

auth = HTTPBasicAuth()


async def get_uow() -> Any:
    """
    Get the unit of work.

    :yield: UnitOfWork
    """
    session = AsyncSession(engine, expire_on_commit=True)
    try:
        yield UnitOfWork(session)
    except Exception:
        await session.rollback()
    finally:
        await session.close()


def user_service_dependency(uow: UnitOfWork = get_uow()) -> UserService:
    """
    Get the user service.

    :param uow: unit of work.
    :return: UserService
    """
    return UserService(uow)


def transaction_service_dependency(uow: UnitOfWork = get_uow()) -> TransactionService:
    """
    Get the transaction service.

    :param uow: unit of work.
    :return: TransactionService
    """
    return TransactionService(uow)


def account_service_dependency() -> AccountService:
    """
    Get the account service.

    :return: AccountService
    """
    uow: UnitOfWork = get_uow()
    return AccountService(uow)
