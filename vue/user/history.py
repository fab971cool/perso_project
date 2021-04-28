from PySide6.QtWidgets import  QVBoxLayout, QPushButton, QWidget, QLineEdit, QFormLayout, QComboBox
from controller.user import UserController

class showHistoryQT(QWidget):

    def __init__(self, user_controller: UserController, user):
        self._user_controller = user_controller
        super().__init__()

        self.user = user
        self.first_name = QLineEdit(user.firstname)
        self.last_name = QLineEdit(user.lastname)

        self.setup()

    def setup(self):
        outerLayout = QVBoxLayout()

        self.setLayout(outerLayout)
