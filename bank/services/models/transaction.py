from apiflask import Schema
from apiflask.fields import Float, Integer
from apiflask.validators import Range


class DepositRequest(Schema):
    """Deposit Request Schema."""

    amount = Float(required=True, validate=Range(min=0))
    account_id = Integer(required=True)


class DepositResponse(Schema):
    """Deposit Response Schema."""

    account_id = Integer(required=True)


class WithdrawRequest(Schema):
    """Withdraw Request Schema."""

    amount = Float(required=True, validate=Range(min=0))
    account_id = Integer(required=True)


class WithdrawResponse(Schema):
    """Withdraw Response Schema."""

    account_id = Integer(required=True)
