from typing import Any, Dict

from apiflask import APIBlueprint

from bank.api.dependencies.services import auth, user_service_dependency
from bank.services.models import user as user_models
from bank.services.user import UserService

router = APIBlueprint("user", __name__)


@router.post("")
@router.auth_required(auth=auth)
@router.input(user_models.CreateUserRequest(partial=True))
@router.output(user_models.CreateUserResponse)
def create_user_api(
    json_data: Dict[str, Any],
    user_service: UserService = user_service_dependency(),
) -> Dict[str, Any]:
    """
    Create user.

    :param json_data: user data.
    :param user_service: user service.
    :return: create user response.
    """
    return user_service.create_user(json_data)


@router.post("/login")
@router.input(user_models.LoginRequest)
@router.output(user_models.LoginResponse)
def login(
    json_data: Dict[str, Any],
    user_service: UserService = user_service_dependency(),
) -> Dict[str, Any]:
    """
    Login user.

    :param json_data: login data.
    :param user_service: user service.
    :return: login response.
    """
    return user_service.login(json_data)
