from typing import Any, Dict

from sqlalchemy import Column, DateTime, String

from bank.db.mappings.base import BaseMapping


class User(BaseMapping):
    """User Mapping."""

    name = Column(String)
    cpf = Column(String, unique=True)
    birth_date = Column(DateTime)
    username = Column(String, unique=True)
    password = Column(String)

    def __repr__(self) -> str:
        return f"<User(name={self.name}, cpf={self.cpf})>"

    def to_dict(self) -> Dict[str, Any]:
        """
        Return a dict representation of the User.

        :return: User dict representation.
        """
        return {
            "id": self.id,
            "name": self.name,
            "cpf": self.cpf,
            "birth_date": self.birth_date,
        }
