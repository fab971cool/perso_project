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

        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QFormLayout()
        # Add a label and a line edit to the form layout

        Layout.addRow("First Name", self.first_name)
        Layout.addRow("Last Name", self.last_name)

        self.type.addItem("admin")
        self.type.addItem("user")
        Layout.addRow("Account type", self.type)

        ValidationLayout = QVBoxLayout()

        btn_add = QPushButton('Add user', self)
        btn_add.clicked.connect(self.addUser)
        btn_add.resize(btn_add.sizeHint())
        btn_add.move(0, 0)

        ValidationLayout.addWidget(btn_add)

        self.setGeometry(100, 100, 200, 150)
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
        self._admin_controller.create_user_admin(self.first_name.text(), self.last_name.text(), self.type.currentText())

        members = self._admin_controller.list_users()

        print("Members: ")
        for member in members:
            print(member)
        self.close()
