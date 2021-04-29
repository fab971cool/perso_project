from PySide6.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QWidget
#from vue.window import BasicWindow
from controller.admin import adminController
from controller.user import UserController


class EditUserQt(QWidget):
    def __init__(self, admin_controller: adminController, user :UserController):
        self._admin_controller = admin_controller
        super().__init__()

        # definit les types de 'boites' qui seront utilisées
        self.first_name = QLineEdit()
        self.last_name = QLineEdit()

        self.user = user
        self.get_user_name(self.user)
        self.setup()

    def setup(self):
        outerLayout = QVBoxLayout()
        Layout = QFormLayout()

        Layout.addRow("First Name", self.first_name)
        Layout.addRow("Last Name", self.last_name)

        # Layout pour les boutons de validation
        ButtonLayout = QVBoxLayout()

        btn_edit = QPushButton('Delete User', self)
        btn_edit.clicked.connect(self.EditUser)
        btn_edit.resize(btn_edit.sizeHint())
        btn_edit.move(90, 100)

        ButtonLayout.addWidget(btn_edit)

        btn_cancel = QPushButton('Cancel', self)
        # btn_cancel.clicked.connect(self.EditUser)
        btn_cancel.resize(btn_cancel.sizeHint())
        btn_cancel.move(90, 100)

        ButtonLayout.addWidget(btn_cancel)

        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle('Admin Edit User')

        # permet de rajouter les layouts dans le principale
        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ButtonLayout)

        self.setLayout(outerLayout)
        self.show()

    def editUser(self):
        # Show subscription formular
        data = {'firstname': self.first_name.text(), 'lastname': self.last_name.text(), 'type': 'user'}
        self._member_controller.update_member(self.user, data)
        self.close()

    def get_user_name(self, user):
        user = self._admin_controller.get_user(user.id)
        self.first_name.setText(user.firstname)
        self.last_name.setText(user.lastname)