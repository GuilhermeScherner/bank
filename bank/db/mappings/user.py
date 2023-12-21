from typing import Any, Dict

from bank.constants import CPF_FIELD_LENGTH, MAX_FIELD_LENGTH, NAME_FIELD_LENGTH
from bank.db.mappings.base import BaseMapping, db


class User(BaseMapping):
    """User Mapping."""

    name = db.Column(db.String(NAME_FIELD_LENGTH))
    account = db.relationship(
        "Account",
        back_populates="user",
        uselist=False,
        primaryjoin="User.id == Account.user_id",
    )
    cpf = db.Column(db.String(CPF_FIELD_LENGTH), unique=True)
    birth_date = db.Column(db.DateTime)
    username = db.Column(db.String(MAX_FIELD_LENGTH), unique=True)
    password = db.Column(db.String(MAX_FIELD_LENGTH))

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
