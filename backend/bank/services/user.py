from typing import Any, Dict, cast

import jwt
import werkzeug
from apiflask import HTTPError

from bank.constants import UNAUTHORIZED
from bank.db.mappings.account import Account
from bank.db.mappings.user import User
from bank.services.base import BaseService
from bank.settings import settings


class UserService(BaseService):
    """User service."""

    def create_user(
        self,
        user_data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Create a user.

        :param user_data: CreateUserRequest
        :return: CreateUserResponse
        """
        hashed_password = werkzeug.security.generate_password_hash(
            cast(str, user_data["password"]),
        )
        user = User(
            name=user_data["name"],
            username=user_data["username"],
            birth_date=user_data["birth_date"],
            cpf=user_data["cpf"],
            password=hashed_password,
        )
        new_user = self.repo.user.add(user)
        account = Account(
            user_id=new_user.id,
            balance=0,
            account_type=1,
        )
        self.repo.account.add(account)
        return new_user.to_dict()

    def login(self, login_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Login a user.

        :param login_data: LoginRequest
        :return: LoginResponse
        :raises HTTPError: if username or password is invalid.
        """
        user = self.repo.user.get_by_username(cast(str, login_data["username"]))
        if not user:
            raise HTTPError(
                UNAUTHORIZED["code"],
                UNAUTHORIZED["message"].format("username."),
            )

        password = cast(str, login_data["password"])
        if werkzeug.security.check_password_hash(user.password, password):
            token = jwt.encode(
                {"user_id": user.id, "username": user.username},
                settings.bank_secret_key,
                algorithm="HS256",
            )
            return {"token": token}
        raise HTTPError(
            UNAUTHORIZED["code"],
            UNAUTHORIZED["message"].format("Password."),
        )
