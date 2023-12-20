from apiflask import APIBlueprint

from bank.api.dependencies.services import auth, transaction_service_dependency
from bank.services.models import transaction as transaction_model
from bank.services.transaction import TransactionService

router = APIBlueprint("transaction", __name__)


@router.post("/deposit")
@auth.login_required
@router.input(transaction_model.DepositRequest)
@router.output(transaction_model.DepositResponse)
async def deposit(
    deposit_model: transaction_model.DepositRequest,
    transaction_service: TransactionService = transaction_service_dependency(),
) -> transaction_model.DepositResponse:
    """
    Deposit money into an account.

    :param deposit_model: DepositRequest
    :param transaction_service: TransactionService
    :return: DepositResponse
    """
    result = await transaction_service.deposit(deposit_model)
    return transaction_model.DepositResponse(**result)


@router.post("/withdraw")
@auth.login_required
@router.input(transaction_model.WithdrawRequest)
@router.output(transaction_model.WithdrawResponse)
async def withdraw(
    withdraw_model: transaction_model.WithdrawRequest,
    transaction_service: TransactionService = transaction_service_dependency(),
) -> transaction_model.WithdrawResponse:
    """
    Withdraw money from an account.

    :param withdraw_model: WithdrawRequest
    :param transaction_service: TransactionService
    :return: WithdrawResponse
    """
    result = await transaction_service.withdraw(withdraw_model)
    return transaction_model.WithdrawResponse(**result)
