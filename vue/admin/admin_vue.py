from vue.user.user_vue import userVue
from PySide6.QtWidgets import QVBoxLayout, QPushButton
from vue.admin.add import AddUserQt


class adminVue (userVue):

    def __init__(self, user, admincontroller):
        super().__init__(user, admincontroller)
        self.setWindowTitle("Admin")
        self.upgrade()

    def upgrade(self):

        adminLayout = QVBoxLayout()

        add_user_btn = QPushButton("add user", self)
        add_user_btn.clicked.connect(self.addUser)
        add_user_btn.resize(add_user_btn.sizeHint())
        add_user_btn.move(65, 230)

        search_user_btn = QPushButton("edit user", self)
        search_user_btn.clicked.connect(self.searchUser)
        search_user_btn.resize(search_user_btn.sizeHint())
        search_user_btn.move(145, 230)

        add_seance_btn = QPushButton("add seance", self)
        add_seance_btn.clicked.connect(self.addSeance)
        add_seance_btn.resize(add_seance_btn.sizeHint())
        add_seance_btn.move(65, 290)

        edit_seance_btn = QPushButton("edit seances", self)
        edit_seance_btn.clicked.connect(self.editSeance)
        edit_seance_btn.resize(edit_seance_btn.sizeHint())
        edit_seance_btn.move(145, 290)

        adminLayout.addWidget(add_user_btn)
        adminLayout.addWidget(search_user_btn)
        adminLayout.addWidget(add_seance_btn)
        adminLayout.addWidget(edit_seance_btn)

        self.mainLayout.addLayout(adminLayout)
        self.setGeometry(100, 100, 300, 350)
        self.setFixedSize(self.size())

    def addUser(self):
        self.Vue = AddUserQt(self.controller)
        self.show()

    def searchUser(self):
        pass

    def addSeance(self):
        pass

    def editSeance(self):
        pass
