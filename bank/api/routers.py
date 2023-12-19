from apiflask import APIFlask


def include_router(app: APIFlask) -> APIFlask:
    """
    Include all routers in the app.

    :param app: application
    :return: application with routers
    """
    return app
