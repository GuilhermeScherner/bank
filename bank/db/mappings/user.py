from sqlalchemy import Column, Integer, String

from bank.db.mappings.base import BaseMapping


class User(BaseMapping):
    name = Column(String(64))
    cpf = Column(String(11), unique=True)
    birth_date = Column(String(10))

    def __repr__(self):
        return "<User(name='%s', cpf='%s')>" % (self.name, self.cpf)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'cpf': self.cpf,
            'birth_date': self.birth_date,
        }