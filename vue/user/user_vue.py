from PySide6.QtWidgets import  QVBoxLayout, QPushButton, QWidget , QLineEdit, QFormLayout, QMessageBox, QLabel
from vue.user.update import UpdateUserQT
from vue.user.history import showHistoryQT


class userVue(QWidget):

    def __init__(self, user, controller):
        super().__init__()
        self.user = user
        self.controller = controller
        self.setWindowTitle("User")
        self.setup()
        self.Vue =None

    def setup(self):
        windowLayout = QVBoxLayout()
        self.label = QLabel("Welcome {}  {} ;".format(self.user.firstname, self.user.lastname), self)
        self.label.move(20, 40)

        search = QPushButton("search a show/movie", self)
        search.clicked.connect(self.search)
        search.resize(search.sizeHint())
        search.move(90, 70)

        seance_list = QPushButton("see the list of film shows", self)
        seance_list.clicked.connect(self.list_seances)
        seance_list.resize(seance_list.sizeHint())
        seance_list.move(80, 110)

        movie_list = QPushButton("see the list of movies", self)
        movie_list.clicked.connect(self.list_movies)
        movie_list.resize(movie_list.sizeHint())
        movie_list.move(90, 150)


        update_btn = QPushButton("Update your data", self)
        update_btn.clicked.connect(self.update_account)
        update_btn.resize(update_btn.sizeHint())
        update_btn.move(150, 190)


        history_btn = QPushButton("see your history", self)
        history_btn.clicked.connect(self.history)
        history_btn.resize(history_btn.sizeHint())
        history_btn.move(40, 190)

        windowLayout.addWidget(self.label)
        windowLayout.addWidget(search)
        windowLayout.addWidget(seance_list)
        windowLayout.addWidget(movie_list)
        windowLayout.addWidget(update_btn)
        windowLayout.addWidget(history_btn)

        self.setGeometry(100, 100, 300, 250)
        self.setFixedSize(self.size())

    def update_account(self):
        self.Vue = UpdateUserQT(self)
        self.Vue.show()


    def history(self):
        self.Vue = showHistoryQT(self.controller, self.user)
        self.Vue.show()

    def search(self):
        pass

    def list_seances(self):
        pass

    def list_movies(self):
        pass
