from apiflask import Schema
from apiflask.fields import Date, String
from apiflask.validators import Length

CPF_LENGTH = 11


class CreateUserRequest(Schema):
    """Create User Response Schema."""

    name = String(required=True)
    username = String(required=True, validate=Length(1))
    birth_date = Date(required=True)
    cpf = String(required=True, validate=Length(CPF_LENGTH, CPF_LENGTH))
    password = String(required=True, validate=Length(1))


class CreateUserResponse(Schema):
    """Create User Response Schema."""

    username = String(required=True)


class LoginRequest(Schema):
    """Login Request Schema."""

    username = String(required=True, validate=Length(1))
    password = String(required=True, validate=Length(1))


class LoginResponse(Schema):
    """Login Response Schema."""

    user = String(required=True)
    access_token = String(required=True)
