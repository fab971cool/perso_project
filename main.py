import sys

from model.database import DatabaseEngine
from PySide6.QtWidgets import QApplication
from vue.login import LoginWindow
from vue.user.add import AddUserQt
from controller.admin import adminController

if __name__ == "__main__":
    databaseEngine = DatabaseEngine(url='sqlite:///pathesiea.db')
    databaseEngine.create_database()
    app = QApplication(sys.argv)
    print("test")
    admin = adminController(databaseEngine)
    test = AddUserQt()

    login = LoginWindow(databaseEngine)
    app.exec_()

