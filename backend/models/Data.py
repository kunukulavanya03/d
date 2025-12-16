from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    description = Column(String)
    user = relationship('User', backref='data')

    def __init__(self, name, description, user_id):
        self.name = name
        self.description = description
        self.user_id = user_id

    def __repr__(self):
        return f'Data({self.name}, {self.description})'