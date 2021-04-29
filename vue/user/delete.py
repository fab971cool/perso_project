from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget, QLineEdit, QFormLayout, QComboBox
from controller.admin import adminController
from controller.user import UserController


class DeleteUserQt(QWidget):

    def __init__(self, admin_controller: adminController, user :UserController):
        self._admin_controller = admin_controller
        super().__init__()

        # definit les types de 'boites' qui seront utilisées
        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.type = QComboBox() # pas possible mais pour les tests

        self.user = user
        self.get_user_name(self.user)
        self.setup()

    def setup(self):

        outerLayout = QVBoxLayout()
        Layout = QFormLayout()

        self.first_name.setEnabled(False)
        Layout.addRow("First Name", self.first_name)
        self.last_name.setEnabled(False)
        Layout.addRow("Last Name", self.last_name)
        self.type.setEnabled(False)
        Layout.addRow("Account type", self.type)

        # Layout pour les boutons de validation
        ButtonLayout = QVBoxLayout()

        btn_del = QPushButton('Delete User', self)
        btn_del.clicked.connect(self.DeleteUser)
        btn_del.resize(btn_del.sizeHint())
        btn_del.move(90, 100)

        ButtonLayout.addWidget(btn_del)

        #self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('Admin delete User')

        # permet de rajouter les layouts dans le principale
        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ButtonLayout)

        self.setLayout(outerLayout)
        self.show()


    def DeleteUser(self):
        self._admin_controller.delete_user(self.user)
        members = self._admin_controller.list_users()

        print("Members: ")
        for member in members:
            print(member)

    def get_user_name(self, user):
        user = self._admin_controller.get_user(user.id)
        self.first_name.setText(user.firstname)
        self.last_name.setText(user.lastname)
        self.type.setCurrentText(user.type)

