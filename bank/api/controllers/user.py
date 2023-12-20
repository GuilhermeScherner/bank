from apiflask import APIBlueprint

from bank.api.dependencies.services import auth, user_service_dependency
from bank.services.models import user as user_models
from bank.services.user import UserService

router = APIBlueprint("user", __name__)


@router.post("")
@auth.login_required
@router.input(user_models.CreateUserRequest)
@router.output(user_models.CreateUserResponse)
async def create_user(
    user_data: user_models.CreateUserRequest,
    user_service: UserService = user_service_dependency(),
) -> user_models.CreateUserResponse:
    """
    Create user.

    :param user_data: user data.
    :param user_service: user service.
    :return: create user response.
    """
    result = await user_service.create_user(user_data)
    return user_models.CreateUserResponse(**result)


@router.post("/login")
@router.input(user_models.LoginRequest)
@router.output(user_models.LoginResponse)
async def login(
    login_data: user_models.LoginRequest,
    user_service: UserService = user_service_dependency(),
) -> user_models.LoginResponse:
    """
    Login user.

    :param login_data: login data.
    :param user_service: user service.
    :return: login response.
    """
    result = await user_service.login(login_data)
    return user_models.LoginResponse(**result)
