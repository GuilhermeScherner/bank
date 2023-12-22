from typing import Any, Dict

MINIMUM_FIELD_LENGTH = 1
MAXIMUM_FIELD_LENGTH = 99
MAXIMUM_NAME_LENGTH = 299
MAX_FIELD_LENGTH = 300
NAME_FIELD_LENGTH = 300
CPF_FIELD_LENGTH = 11
NOT_FOUND: Dict[str, Any] = {"code": 404, "message": "{} not found"}  # noqa: P103
UNAUTHORIZED: Dict[str, Any] = {"code": 401, "message": "Unauthorized {}"}  # noqa: P103
