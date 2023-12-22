from apiflask import APIFlask

from bank.api.controllers import account, transaction, user


def include_router(app: APIFlask) -> APIFlask:
    """
    Include all routers in the app.

    :param app: application
    :return: application with routers
    """
    app.register_blueprint(user.router, url_prefix="/user")
    app.register_blueprint(account.router, url_prefix="/account")
    app.register_blueprint(transaction.router, url_prefix="/transaction")
    return app
