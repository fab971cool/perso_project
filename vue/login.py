from PySide6.QtWidgets import  QVBoxLayout, QPushButton, QWidget , QLineEdit, QFormLayout


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.lastname = QLineEdit()
        self.firstname = QLineEdit()
        self.setup()

    def setup(self):

        windowLayout = QVBoxLayout()

        layout = QFormLayout()

        layout.addRow("Prenom", self.firstname)
        layout.addRow("Nom", self.lastname)

        ValidationLayout = QVBoxLayout()
        validation = QPushButton("Valider", self)
        validation.clicked.connect(self.login)
        validation.resize(validation.sizeHint())
        validation.move(90, 100)
        ValidationLayout.addWidget(validation)

        windowLayout.addLayout(layout)
        windowLayout.addLayout(ValidationLayout)
        self.setLayout(windowLayout)
        self.show()

    def login(self):
        pass

    def refresh(self):
        pass

