from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.user import User
from model.dao.dao import DAO


class UserDAO(DAO):

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, firstname: str, lastname: str):
        try:
            return self._database_session.query(User).filter_by(firstname=firstname, lastname=lastname)
        except NoResultFound:
            raise Exception("Ressource not found.")

    def get_User(self, id: int):
        try:
            return self._database_session.query(User).filter_by(id=id).order_by(User.firstname).one()
        except NoResultFound:
            raise Exception("Ressource not found.")

    def get_all(self):

        try:
           return self._database_session.query(User).order_by(User.firstname).all()
        except NoResultFound:
            raise Exception("Ressource not found.")

    def create(self, firstname: str, lastname: str, type: str):

        try:
            user = User(firstname=firstname, lastname=lastname, type=type)
            self._database_session.add(user)
            self._database_session.flush()
        except IntegrityError:
            raise Exception("User already exists")
        return user

    def update(self, user: User, data: dict):
        if 'firstname' in data:
            user.firstname = data['firstname']
        if 'lastname' in data:
            user.lastname = data['lastname']
        if 'type' in data:
            user.type = data['type']
        try:
            self._database_session.merge(user)
            self._database_session.flush()
        except IntegrityError:
            raise Exception('Error data may be malformed')
        return user

    def delete(self, user):
        try:
            self._database_session.delete(user)
        except SQLAlchemyError as e:
            raise Exception(str(e))

