from typing import Any, Dict

from bank.services.base import BaseService
from bank.services.models import user as user_model


class UserService(BaseService):
    """User service."""

    async def create_user(
        self,
        user_data: user_model.CreateUserRequest,
    ) -> Dict[str, Any]:
        """
        Create a user.

        :param user_data: CreateUserRequest
        :return: CreateUserResponse
        """
        return {}

    async def login(self, login_data: user_model.LoginRequest) -> Dict[str, Any]:
        """
        Login a user.

        :param login_data: LoginRequest
        :return: LoginResponse
        """
        return {}
