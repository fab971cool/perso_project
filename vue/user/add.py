from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget, QLineEdit, QFormLayout, QComboBox
from controller.admin import adminController


class AddUserQt(QWidget):

    def __init__(self, admin_controller: adminController):
        self._admin_controller = admin_controller
        super().__init__()

        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.type = QComboBox() # pas possible mais pour les tests

        self.setup()

    def setup(self):

        # Layout principal = Layout
        outerLayout = QVBoxLayout()
        Layout = QFormLayout()

        Layout.addRow("First Name", self.first_name)
        Layout.addRow("Last Name", self.last_name)

        self.type.addItem("user")
        self.type.addItem("admin")
        Layout.addRow("Account type", self.type)

        ValidationLayout = QVBoxLayout()

        btn_add = QPushButton('Add user', self)
        btn_add.clicked.connect(self.addUser)
        btn_add.resize(btn_add.sizeHint())
        btn_add.move(90, 1000)

        ValidationLayout.addWidget(btn_add)

        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle('Admin add User')

        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ValidationLayout)

        self.setLayout(outerLayout)
        self.show()


    def addUser(self):
        # Show subscription formular
        data = {'firstname': self.first_name.text(),
                'lastname': self.last_name.text(),
                'type': self.type.currentText()}
        print(data)
        self._admin_controller.create_user(self.first_name.text(), self.last_name.text(), self.type.currentText())

        members = self._admin_controller.list_users()

        print("Members: ")
        for member in members:
            print(member)

