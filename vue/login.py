from PySide6.QtWidgets import QVBoxLayout, QPushButton, QWidget, QLineEdit, QFormLayout, QMessageBox, QLabel
from controller.functions import login
from vue.user.user_vue import userVue
from vue.admin.admin_vue import adminVue
from vue.user.add import CreateUserQt
from controller.user import UserController


class LoginWindow(QWidget):

    def __init__(self, database_engine):
        super().__init__()
        self.db = database_engine
        self.lastname = QLineEdit()
        self.firstname = QLineEdit()
        self.setWindowTitle("Login")
        self.Vue =None
        self.setup()

    def setup(self):

        windowLayout = QVBoxLayout()

        layout = QFormLayout()

        layout.addRow("firstname", self.firstname)
        layout.addRow("lastname", self.lastname)

        ValidationLayout = QVBoxLayout()
        validation = QPushButton("Validate", self)
        validation.clicked.connect(self.login)
        validation.resize(validation.sizeHint())
        validation.move(90, 80)

        label = QLabel("New client, sign-in",self)
        label.move(90,70)

        signIn = QPushButton("Sign-in", self)
        signIn.clicked.connect(self.signIn)
        signIn.resize(signIn.sizeHint())
        signIn.move(90, 100)

        ValidationLayout.addWidget(validation)
        ValidationLayout.addWidget(signIn)

        windowLayout.addLayout(layout)
        windowLayout.addLayout(ValidationLayout)
        self.setGeometry(100, 100, 300, 170)
        self.setLayout(windowLayout)
        self.show()
        self.setFixedSize(self.size())

    def login(self):
        try:
            if self.firstname == '' or self.lastname=='':
                raise Exception('Veuillez entrer un nom et un prenom.')

            user, controller = login(self.firstname.text(), self.lastname.text(), self.db)

            if user is None:
                raise Exception("This user doesn't exist, verify your informations or create an account")
            elif user.type == "user":
                self.close()
                self.Vue = userVue(user, controller)
                self.Vue.show()

            elif user.type == "admin":
                self.close()
                self.Vue = adminVue(user, controller)
                self.Vue.show()

        except Exception as e:

            msgBox = QMessageBox()
            if str(e) == "Invalid data":
                msgBox.setText("The user firstname and lastname must contain between 2 and 50 letters ")
            else:
                msgBox.setText(str(e))
            msgBox.setWindowTitle("Warning")
            msgBox.exec_()

    def signIn(self):
        self.close()
        controller = UserController(self.db)
        self.Vue = CreateUserQt(controller)
        self.Vue.show()

