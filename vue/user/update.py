from PySide6.QtWidgets import  QVBoxLayout, QPushButton, QWidget, QLineEdit, QFormLayout


class UpdateUserQT(QWidget):

    def __init__(self, user_vue):
        self._user_vue = user_vue
        super().__init__()

        self.first_name = QLineEdit(user_vue.user.firstname)
        self.last_name = QLineEdit(user_vue.user.lastname)
        self.setWindowTitle("Update your account")
        self.Vue = None
        self.setup()

    def setup(self):
        outerLayout = QVBoxLayout()

        Layout = QFormLayout()
        Layout.addRow("New firstname", self.first_name)
        Layout.addRow("New lastname", self.last_name)

        ValidationLayout = QVBoxLayout()
        btn_add = QPushButton('Update my account', self)
        btn_add.clicked.connect(self.updateUser)
        btn_add.resize(btn_add.sizeHint())
        btn_add.move(90, 100)

        ValidationLayout.addWidget(btn_add)
        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ValidationLayout)

        self.setGeometry(100, 100, 350, 200)
        self.setFixedSize(self.size())
        self.setLayout(outerLayout)

    def updateUser(self):
        data = {'firstname': self.first_name.text(), 'lastname': self.last_name.text()}
        self._user_vue.controller.update_user(self._user_vue.user, data)
        self._user_vue.label.setText("Welcome {}  {} ;".format(self._user_vue.user.firstname, self._user_vue.user.lastname))
        self._user_vue.label.resize(self._user_vue.label.sizeHint())
        self.close()