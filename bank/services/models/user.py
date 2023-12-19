from apiflask import Schema
from apiflask.fields import Date, String
from marshmallow.validate import Length


class CreateUserResponse(Schema):
    """Create User Response Schema."""

    name = String(required=True, validate=Length(0, 10))
    email = String(required=True, validate=Length(0, 10))
    username = String(required=True, validate=Length(0, 10))
    birth_date = Date(required=True, validate=Length(0, 10))
    cpf = String(required=True, validate=Length(0, 10))
    password = String(required=True, validate=Length(0, 10))
