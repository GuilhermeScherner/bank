from sqlalchemy import Column, Integer, ForeignKey, Float, Boolean, String
from sqlalchemy.orm import relationship

from bank.db.mappings.base import BaseMapping


class Account(BaseMapping):
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref='accounts')
    balance = Column(Float, default=0.0)
    daily_withdrawal_limit = Column(Float, default=1000.0)  # daily withdrawal
    is_active = Column(Boolean, default=True)
    account_type = Column(String(10), default='current')

    def __repr__(self):
        return "<Account(user_id='%s', balance='%s')>" % (self.user_id, self.balance)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'balance': self.balance,
        }
