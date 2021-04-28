from PySide6.QtWidgets import  QVBoxLayout, QPushButton, QWidget, QLineEdit, QFormLayout, QComboBox
from controller.user import UserController
from vue.user.user_vue import userVue

class CreateUserQt(QWidget):

    def __init__(self, user_controller: UserController):
        self._user_controller = user_controller
        super().__init__()

        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.setup()
        self.Vue = None

    def setup(self):

        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QFormLayout()
        # Add a label and a line edit to the form layout

        Layout.addRow("First Name", self.first_name)
        Layout.addRow("Last Name", self.last_name)

        ValidationLayout = QVBoxLayout()

        btn_add = QPushButton('Create my account', self)
        btn_add.clicked.connect(self.addUser)
        btn_add.resize(btn_add.sizeHint())
        btn_add.move(0, 0)

        ValidationLayout.addWidget(btn_add)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('Create User')

        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ValidationLayout)

        self.setLayout(outerLayout)

    def addUser(self):
        # Show subscription formular
        user = self._user_controller.create_user(self.first_name.text(),self.last_name.text())
        self.close()
        self.Vue = userVue(user, self._user_controller)
        self.Vue.show()




