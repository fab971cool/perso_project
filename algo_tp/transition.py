from etats import * 

class Transition:
    def __init__(self, etatA, etq=None): # etats = etat()
        self.etatA = etatA
        self.etq = etq
        return None

    def ajoutTransitionLettre(self, etatB, etq):
        self.etatB = etatB
        self.etq = etq
        return None


    # Permet de tester si une lettre passe cette transition
    # renvoie 1 si transition ok 0 sinon
    def verifTransition(self, lettre):
        if (self.etq == lettre):
            return 1
        return 0