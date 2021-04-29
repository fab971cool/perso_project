import sys

from model.database import DatabaseEngine
from PySide6.QtWidgets import QApplication
from vue.login import LoginWindow


if __name__ == "__main__":
    databaseEngine = DatabaseEngine(url='sqlite:///pathesiea.db')
    databaseEngine.create_database()
    app = QApplication(sys.argv)
    login = LoginWindow(databaseEngine)
    app.exec_()

