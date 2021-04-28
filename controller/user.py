import re

from model.dao.user_dao import UserDAO


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

    # bien
    def update_user(self, user, data):

        self.check_data(data)
        with self._database_engine.new_session() as session:
            user = UserDAO(session).update(user, data)
            return user

    # bien
    def update_history(self, user, new_seance_id):
        with self._database_engine.new_session() as session:
            user = UserDAO(session).append_history(user, new_seance_id)
            return user

    # bien
    def delete_user(self, user):
        with self._database_engine.new_session() as session:
            UserDAO(session).delete(user)


    def get_history(self, user):
        return user.history

    check_data = staticmethod(_check_data)

