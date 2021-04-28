import uuid

from sqlalchemy import Column, String, UniqueConstraint, PickleType
from sqlalchemy.ext.mutable import MutableList

from model.mapping import Base


class User(Base):
    __tablename__ = 'users'
    __table_args__ = (UniqueConstraint('firstname', 'lastname'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    history = Column(MutableList.as_mutable(PickleType), default=[])
    type = Column(String(10), nullable=False)


    def __repr__(self):
        return "<Member(%s %s %s %s)>" % (self.firstname, self.lastname.upper(), self.type, self.id)

