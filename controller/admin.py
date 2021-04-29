from controller.user import *


class adminController(UserController):

    def __init__(self, database_engine):
        super().__init__(database_engine)

    # pour admin
    def list_users(self):
        with self._database_engine.new_session() as session:
            users = UserDAO(session).get_all()
        return users

    # pour admin
    def get_user(self, user_id):
        with self._database_engine.new_session() as session:
            user = UserDAO(session).get(user_id)
        return user

    # pour admin
    def search_user(self, firstname: str, lastname: str):
        with self._database_engine.new_session() as session:
            user = UserDAO(session).get_User(firstname, lastname)
            return user

    def create_user_admin(self, firstname: str, lastname: str, type: str):

        self.check_data({'firstname': firstname, 'lastname': lastname, 'type': type})

        try:
            with self._database_engine.new_session() as session:
                user = UserDAO(session).create({'firstname': firstname, 'lastname': lastname, 'type': type})
                return user
        except Exception as e:
            raise e