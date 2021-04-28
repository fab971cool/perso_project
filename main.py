from controller.user import UserController
from model.database import DatabaseEngine


if __name__ == "__main__":
    databaseEngine = DatabaseEngine(url='sqlite:///pathesiea.db')
    databaseEngine.create_database()
    user_controller = UserController(databaseEngine)
    user_controller.create_user('testt', 'te', 'user')
    print('Before update')
    user_list = user_controller.list_users()
    for u in user_list:
        print(u)
        u.update
        user_controller.delete_user(u.id)


    for u in user_list:
        print(u)
        print("yes")
