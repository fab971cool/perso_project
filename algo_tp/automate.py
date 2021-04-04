from transition import Transition

class Automate:
    def __init__(self):
        self.listEtat = []
        self.alpha = []
        self.nbInit=None
        self.nbFin=None
        return None

    def recupEtats(self, etat):
        self.listEtat.append(etat)
        return 0
    def recupAlphabet(self, alphaB ):
        self.alpha.append(alphaB)
        return 0

    def afficheEtats(self):
        for i in self.listEtat :
            print(i.nbre)
        return None

    def setInitAcceptant(self, nbrInit, nbrFin):
        for i in range(len(self.listEtat)):
            if ( i == int(nbrInit)):
                self.listEtat[i].setInitial(True)
            if (i == int(nbrFin)):
                self.listEtat[i].setAcceptant(True)
        return None


    # on cree une transition independante qui sera lié à un état
    def ajoutTransition(self, nbrEtatA, nbrEtatB, etq):
        self.transition = Transition(self.listEtat[nbrEtatA])
        self.transition.ajoutTransitionLettre(self.listEtat[nbrEtatB], etq)
        
        # on fait la liaison entre l'etat et la transition ( append )
        self.listEtat[nbrEtatA].listTransition.append(self.transition)
        return None