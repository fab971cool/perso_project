import sys
from transition import *


class Etats():
    def __init__(self, nombre=None, acceptant=False, initial=False):
        self.nbre = nombre
        self.acceptant = acceptant
        self.initial = initial
        self.listTransition = []

    def setEtat(self, nombre, acceptant=False, initial=False):
        self.nbre = nombre
        self.acceptant = acceptant
        self.initial = initial
        return None

    def setAcceptant(self, acceptant=True):
        self.acceptant = acceptant
        return None
    def setInitial(self, initial=True):
        self.initial = initial
        return None