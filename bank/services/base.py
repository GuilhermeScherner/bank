from bank.db.uow import UnitOfWork


class BaseService:
    """Base service."""

    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow
