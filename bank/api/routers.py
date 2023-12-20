from apiflask import APIFlask

from bank.api.controllers import user


def include_router(app: APIFlask) -> APIFlask:
    """
    Include all routers in the app.

    :param app: application
    :return: application with routers
    """
    app.register_blueprint(user.router, url_prefix="/user")
    return app
