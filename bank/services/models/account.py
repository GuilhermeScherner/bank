from apiflask import Schema
from apiflask.fields import Float, Integer
from apiflask.validators import Range


class BalanceRequest(Schema):
    """Deposit Request Schema."""

    account_id = Integer(required=True)


class BalanceResponse(Schema):
    """Deposit Response Schema."""

    balance = Float(required=True)


class ChangeStateRequest(Schema):
    """Change State Request Schema."""

    account_id = Integer(required=True)
    state = Integer(required=True, validate=Range(min=0, max=1))


class ChangeStateResponse(Schema):
    """Change State Response Schema."""

    account_id = Integer(required=True)
    state = Integer(required=True, validate=Range(min=0, max=1))


class OrdersRequest(Schema):
    """Orders Request Schema."""

    account_id = Integer(required=True)
    page = Integer(required=True, validate=Range(min=1))
    page_size = Integer(required=True, validate=Range(min=1))


class OrdersResponse(Schema):
    """Orders Response Schema."""

    account_id = Integer(required=True)
    orders = Integer(required=True)
    page = Integer(required=True, validate=Range(min=1))
    page_size = Integer(required=True, validate=Range(min=1))
    total_pages = Integer(required=True, validate=Range(min=1))
    total_orders = Integer(required=True, validate=Range(min=1))
