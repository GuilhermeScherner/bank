from typing import Any, Dict

from apiflask import APIBlueprint

from bank.api.dependencies.services import auth, transaction_service_dependency
from bank.services.models import transaction as transaction_model
from bank.services.models.user import UserBase
from bank.services.transaction import TransactionService

router = APIBlueprint("transaction", __name__)


@router.patch("/deposit")
@router.auth_required(auth=auth)
@router.input(transaction_model.DepositRequest)
@router.output(transaction_model.DepositResponse)
def deposit(
    json_data: Dict[str, Any],
    transaction_service: TransactionService = transaction_service_dependency(),
) -> Dict[str, Any]:
    """
    Deposit money into an account.

    :param json_data: DepositRequest
    :param transaction_service: TransactionService
    :return: DepositResponse
    """
    user = UserBase(user_id=auth.current_user["id"], username=auth.current_user["username"])  # type: ignore
    json_data.update({"user_id": user.id})
    return transaction_service.deposit(json_data)


@router.patch("/withdraw")
@router.auth_required(auth=auth)
@router.input(transaction_model.WithdrawRequest)
@router.output(transaction_model.WithdrawResponse)
def withdraw(
    json_data: Dict[str, Any],
    transaction_service: TransactionService = transaction_service_dependency(),
) -> Dict[str, Any]:
    """
    Withdraw money from an account.

    :param json_data: WithdrawRequest
    :param transaction_service: TransactionService
    :return: WithdrawResponse
    """
    user = UserBase(user_id=auth.current_user["id"], username=auth.current_user["username"])  # type: ignore
    json_data.update({"user_id": user.id})
    return transaction_service.withdraw(json_data)


@router.get("/orders")
@router.auth_required(auth=auth)
@router.output(transaction_model.OrdersResponse)
def orders(
    transaction_service: TransactionService = transaction_service_dependency(),
) -> Dict[str, Any]:
    """
    Get all orders from an account.

    :param transaction_service: TransactionService
    :return: OrdersResponse
    """
    user = UserBase(user_id=auth.current_user["id"], username=auth.current_user["username"])  # type: ignore

    return transaction_service.orders(user.id)
