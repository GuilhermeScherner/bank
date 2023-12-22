from apiflask import Schema
from apiflask.fields import Float, Integer, List, Nested, DateTime
from apiflask.validators import Range


class DepositRequest(Schema):
    """Deposit Request Schema."""

    amount = Float(required=True, validate=Range(min=0))


class DepositResponse(Schema):
    """Deposit Response Schema."""

    transaction_id = Integer(required=True)


class WithdrawRequest(Schema):
    """Withdraw Request Schema."""

    amount = Float(required=True, validate=Range(min=0))


class WithdrawResponse(Schema):
    """Withdraw Response Schema."""

    transaction_id = Integer(required=True)


class Order(Schema):
    """Orders Response Schema."""

    account_id = Integer(required=True)
    amount = Float(required=True)
    date = DateTime(required=True)


class OrdersResponse(Schema):
    """Orders Request Schema."""

    data = List(Nested(Order))
