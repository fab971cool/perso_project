from PySide6.QtWidgets import  QVBoxLayout, QPushButton, QWidget , QLineEdit, QFormLayout, QMessageBox, QLabel
from controller.functions import login


class LoginWindow(QWidget):

    def __init__(self, database_engine):
        super().__init__()
        self.db = database_engine
        self.lastname = QLineEdit()
        self.firstname = QLineEdit()
        self.setWindowTitle("Login")
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
        #validation.clicked.connect()//todo ajouter page création de compte user
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
            if user == None:
                raise Exception("This user doesn't exist, verify your informations or create an account")


        except Exception as e:

            msgBox = QMessageBox()
            if str(e) == "Invalid data":
                msgBox.setText("The user firstname and lastname must contain between 2 and 50 letters ")
            else:
                msgBox.setText(str(e))
            msgBox.exec_()



    def refresh(self):
        pass

