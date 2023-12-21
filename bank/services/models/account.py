from typing import cast

from apiflask import Schema
from apiflask.fields import Boolean, Float, Integer


class BalanceResponse(Schema):
    """Deposit Response Schema."""

    balance = Float(required=True)


class ChangeStateRequest(Schema):
    """Change State Request Schema."""

    user_id = Integer(data_key="user_id", required=True)
    state = Boolean(data_key="state", required=True)

    def __init__(self, user_id: int | Integer, state: bool) -> None:
        """
        Initialize the user.

        :param user_id: user id.
        :param state: state.
        """
        self.user_id = cast(Integer, user_id)  # noqa: WPS601
        self.state = cast(Boolean, state)  # noqa: WPS601
        super().__init__()


class ChangeStateResponse(Schema):
    """Change State Response Schema."""

    id = Integer(required=True)
