from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget, QLineEdit, QFormLayout, QComboBox, QMessageBox

from PySide6.QtGui import QCloseEvent


# TODO Ajouter la classe dans la classe Mère
# pas besoin d'avoir un objet event car appel lorsque l'on clique sur un bouton
class Validation(QWidget):

    def __init__(self):
        super().__init__()

        self.validation = QMessageBox()
        self.Layout = QVBoxLayout()

        self.setup()

    #TODO Ajouter un bouton pour appeler la fonction quit
    # fonction setup pour les test A SUPPRIMMER
    def setup(self):

        btnTest = QPushButton('Test', self)
        btnTest.clicked.connect(self.quit)
        btnTest.resize(btnTest.sizeHint())
        btnTest.move(90, 100)

        self.Layout.addWidget(btnTest)

        self.setLayout(self.Layout)
        self.show()

    def quit(self, event:QCloseEvent):
        self.validation = QMessageBox.question(self, 'Test', 'Bonjour', QMessageBox.Yes, QMessageBox.No)

        if (self.validation == QMessageBox.Yes):
            return False
        else:
            event.ignore()