from model.mapping import Base
from sqlalchemy.ext.mutable import MutableList
import uuid

from sqlalchemy import Column, String, UniqueConstraint, PickleType, ARRAY

class User(Base):
    __tablename__ = 'users'
    __table_args__ = (UniqueConstraint('firstname', 'lastname'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)

    type = Column(String(10), nullable=False)
    history = Column(ARRAY(String(20)), nullable=True)


    def __repr__(self):
        return "<Member(%s %s %s %s)>" % (self.firstname, self.lastname.upper(), self.type, self.id)