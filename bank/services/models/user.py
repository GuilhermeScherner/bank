from typing import cast

from apiflask import Schema
from apiflask.fields import Date, Integer, String
from apiflask.validators import Length

from bank.constants import (
    CPF_FIELD_LENGTH,
    MAXIMUM_FIELD_LENGTH,
    MAXIMUM_NAME_LENGTH,
    MINIMUM_FIELD_LENGTH,
)


class UserBase(Schema):
    """User Schema."""

    id = Integer(required=True, data_key="user_id")
    username = String(required=True, data_key="username")

    def __init__(self, user_id: int, username: str) -> None:
        """
        Initialize the user.

        :param user_id: user id.
        :param username: username.
        """
        self.id = cast(Integer, user_id)  # noqa: WPS601
        self.username = cast(String, username)  # noqa: WPS601
        super().__init__()


class CreateUserRequest(Schema):
    """Create User Response Schema."""

    name = String(
        required=True,
        validate=Length(MINIMUM_FIELD_LENGTH, MAXIMUM_NAME_LENGTH),
    )
    username = String(
        required=True,
        validate=Length(MINIMUM_FIELD_LENGTH, MAXIMUM_FIELD_LENGTH),
    )
    birth_date = Date(required=True)
    cpf = String(required=True, validate=Length(CPF_FIELD_LENGTH, CPF_FIELD_LENGTH))
    password = String(
        required=True,
        validate=Length(MINIMUM_FIELD_LENGTH, MAXIMUM_FIELD_LENGTH),
    )


class CreateUserResponse(Schema):
    """Create User Response Schema."""

    id = Integer(required=True)
    username = String(required=True)


class LoginRequest(Schema):
    """Login Request Schema."""

    username = String(required=True, validate=Length(1, MAXIMUM_FIELD_LENGTH))
    password = String(required=True, validate=Length(1, MAXIMUM_FIELD_LENGTH))


class LoginResponse(Schema):
    """Login Response Schema."""

    token = String(required=True)
