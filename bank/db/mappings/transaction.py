from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from bank.db.mappings.base import BaseMapping


class Transaction(BaseMapping):
    account_id = Column(Integer, ForeignKey('account.id'))
    account = relationship('Account', backref='transactions')
    amount = Column(Float, default=0.0)

    def __repr__(self):
        return "<Transaction(account_id='%s', amount='%s')>" % (self.account_id, self.amount)

    def to_dict(self):
        return {
            'id': self.id,
            'account_id': self.account_id,
            'amount': self.amount,
            'transaction_date': self.created_at,
        }