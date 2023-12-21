from typing import Any, Dict

from apiflask import APIBlueprint

from bank.api.dependencies.services import account_service_dependency, auth
from bank.services.account import AccountService
from bank.services.models import account as account_model
from bank.services.models.user import UserBase

router = APIBlueprint("account", __name__)


@router.get("/balance")
@router.auth_required(auth=auth)
@router.output(account_model.BalanceResponse)
def balance(
    account_service: AccountService = account_service_dependency(),
) -> Dict[str, Any]:
    """
    Get the balance of an account.

    :param account_service: AccountService
    :return: BalanceResponse
    """
    user = UserBase(user_id=auth.current_user["id"], username=auth.current_user["username"])  # type: ignore
    result = account_service.balance(user.id)
    return {"balance": result["balance"]}


@router.patch("/block")
@router.auth_required(auth=auth)
@router.output(account_model.ChangeStateResponse)
def block(
    account_service: AccountService = account_service_dependency(),
) -> Dict[str, Any]:
    """
    Block an account.

    :param account_service: AccountService
    :return: ChangeStateResponse
    """
    user = UserBase(user_id=auth.current_user["id"], username=auth.current_user["username"])  # type: ignore

    change_state_request = account_model.ChangeStateRequest(
        user_id=user.id,
        state=False,
    )
    response = account_service.change_state(change_state_request)
    return {"id": response["id"]}


@router.patch("/unblock")
@router.auth_required(auth=auth)
@router.output(account_model.ChangeStateResponse)
def unblock(
    account_service: AccountService = account_service_dependency(),
) -> Dict[str, Any]:
    """
    Unblock an account.

    :param account_service: AccountService
    :return: ChangeStateResponse
    """
    user = UserBase(user_id=auth.current_user["id"], username=auth.current_user["username"])  # type: ignore
    change_state_request = account_model.ChangeStateRequest(
        user_id=user.id,
        state=True,
    )
    response = account_service.change_state(change_state_request)
    return {"id": response["id"]}
