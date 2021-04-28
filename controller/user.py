from model.dao.user_dao import UserDAO
import re


def _check_data(data):

    err = False
    if 'firstname' in data:
        if re.fullmatch("^[a-zA-]{2,50}$", data["firstname"]) is None:
            print("The user firstname must contain between 2 and 50 letters ")
            err = True
    if 'lastname' in data:
        if re.fullmatch("^[a-zA-]{2,50}$", data["lastname"]) is None:
            print("The user lastname must contain between 2 and 50 letters ")
            err = True
    if 'type' in data:
        if re.fullmatch("^(user|admin)$", data['type']) is None:
            print("The type must be 'user' or 'admin'")
            err = True

    if err is True:
        raise Exception("Invalid data")


class UserController:

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def list_users(self):
        with self._database_engine.new_session() as session:
            users = UserDAO(session).get_all()
        return users

    def get_user(self, user_id):
        with self._database_engine.new_session() as session:
            user = UserDAO(session).get_User(user_id)
        return user

    def create_user(self, firstname: str, lastname: str, type: str):

        self.check_data({'firstname': firstname, 'lastname': lastname, 'type': type})

        try:
            with self._database_engine.new_session() as session:
                user = UserDAO(session).create({'firstname': firstname, 'lastname': lastname, 'type': type})
                return user
        except Exception as e:
            raise e

    def update_user(self, user_id, data):

        self.check_data(data)
        with self._database_engine.new_session() as session:
            user = UserDAO(session).get(id)
            user = UserDAO(session).update(user, data)
            return user

    def update_history(self, user_id, new_seance_id):
        with self._database_engine.new_session() as session:
            user = UserDAO(session).get_User(user_id)
            user = UserDAO(session).append_history(user, new_seance_id)
            return user

    def delete_user(self, user_id):
        with self._database_engine.new_session() as session:
            user = UserDAO(session).get(user_id)
            UserDAO(session).delete(user)

    def search_user(self, firstname: str, lastname: str):
        with self._database_engine.new_session() as session:
            user = UserDAO(session).get_User(firstname, lastname)
            return user

    check_data = staticmethod(_check_data)
