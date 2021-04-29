from PySide6.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QWidget
#from vue.window import BasicWindow
from controller.admin import adminController
from controller.user import UserController
from edit import EditUserQt

class SearchUserQt(QWidget):
    def __init__(self, admin_controller: adminController):
        self._admin_controller = admin_controller
        super().__init__()

        # definit les types de 'boites' qui seront utilisées
        self.first_name = QLineEdit()
        self.last_name = QLineEdit()

        self.newWindow = None


        self.get_user_name(self.user)
        self.setup()

    def setup(self):
        outerLayout = QVBoxLayout()
        Layout = QFormLayout()

        Layout.addRow("First Name", self.first_name)
        Layout.addRow("Last Name", self.last_name)

        # Layout pour les boutons de validation
        ButtonLayout = QVBoxLayout()

        btn_search = QPushButton('Search User', self)
        btn_search.clicked.connect(self.SearchUser)
        btn_search.resize(btn_search.sizeHint())
        btn_search.move(90, 100)

        ButtonLayout.addWidget(btn_search)

        btn_cancel = QPushButton('Cancel', self)
        # btn_cancel.clicked.connect(self.EditUser)
        btn_cancel.resize(btn_cancel.sizeHint())
        btn_cancel.move(90, 100)

        ButtonLayout.addWidget(btn_cancel)

        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle('Admin Search User')

        # permet de rajouter les layouts dans le principale
        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ButtonLayout)

        self.setLayout(outerLayout)
        self.show()

    def SearchUser(self):
        # Show subscription formular
        user = self._admin_controller.search_user(self.first_name.text(), self.last_name.text())
        if ( self.newWindow is None):
            self.newWindow = EditUserQt(self._admin_controller, user)
        self.newWindow.show()


    def get_user_name(self, user):
        user = self._admin_controller.get_user(user.id)
        self.first_name.setText(user.firstname)
        self.last_name.setText(user.lastname)