from controller.admin import *
from controller.user import *
from controller.user import UserController


def login(prenom, nom, database_engine):

    try:
        user = adminController(database_engine).search_user(prenom, nom)
        if user.type == "admin":
            return user, adminController(database_engine)
        else:
            return user, UserController(database_engine)
    except:
        controller = UserController(database_engine)
        user = None
        return user, controller

