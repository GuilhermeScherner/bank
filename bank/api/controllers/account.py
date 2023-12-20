from apiflask import APIBlueprint

from bank.api.dependencies.services import account_service_dependency, auth
from bank.services.account import AccountService
from bank.services.models import account as account_model

router = APIBlueprint("transaction", __name__)


@router.post("/balance")
@auth.login_required
@router.input(account_model.BalanceRequest)
@router.output(account_model.BalanceResponse)
async def balance(
    balance_request: account_model.BalanceRequest,
    account_service: AccountService = account_service_dependency(),
) -> account_model.BalanceResponse:
    """
    Get the balance of an account.

    :param balance_request: BalanceRequest
    :param account_service: AccountService
    :return: BalanceResponse
    """
    response = await account_service.balance(balance_request)
    return account_model.BalanceResponse(**response)


@router.post("/block")
@auth.login_required
@router.input(account_model.ChangeStateRequest)
@router.output(account_model.ChangeStateResponse)
async def block(
    change_state_request: account_model.ChangeStateRequest,
    account_service: AccountService = account_service_dependency(),
) -> account_model.ChangeStateResponse:
    """
    Block an account.

    :param change_state_request: ChangeStateRequest
    :param account_service: AccountService
    :return: ChangeStateResponse
    """
    response = await account_service.change_state(change_state_request)
    return account_model.ChangeStateResponse(**response)


@router.post("/unblock")
@auth.login_required
@router.input(account_model.ChangeStateRequest)
@router.output(account_model.ChangeStateResponse)
async def unblock(
    change_state_request: account_model.ChangeStateRequest,
    account_service: AccountService = account_service_dependency(),
) -> account_model.ChangeStateResponse:
    """
    Unblock an account.

    :param change_state_request: ChangeStateRequest
    :param account_service: AccountService
    :return: ChangeStateResponse
    """
    response = await account_service.change_state(change_state_request)
    return account_model.ChangeStateResponse(**response)


@router.post("/orders")
@auth.login_required
@router.input(account_model.OrdersRequest)
@router.output(account_model.OrdersResponse)
async def orders(
    orders_request: account_model.OrdersRequest,
    account_service: AccountService = account_service_dependency(),
) -> account_model.OrdersResponse:
    """
    Get all orders from an account.

    :param orders_request: OrdersRequest
    :param account_service: AccountService
    :return: OrdersResponse
    """
    response = await account_service.orders(orders_request)
    return account_model.OrdersResponse(**response)
