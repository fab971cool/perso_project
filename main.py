from controller.functions import login
from model.database import DatabaseEngine


if __name__ == "__main__":
    databaseEngine = DatabaseEngine(url='sqlite:///pathesiea.db')
    databaseEngine.create_database()
    user, controller = login("pierre", "fouquart",databaseEngine)
    print(controller.list_users())
    controller.create_user("testa", "test", "admin")
    print(controller.list_users())


