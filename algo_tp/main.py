import sys 
from etats import *
from transition import *
from automate import *




def verifAfdMot(mot, etat):
	# while(1):
	# 	for i in mot:
	k = 0
	j=0
	while j < len(etat.listTransition):
		# on trouve la lettre = chgt : Etat + lettreMot
		# lorsque k = len(mot) ou j = len(Transition)-> etat acceptant ?
		if ( etat.listTransition[j].verifTransition(mot[k])): #mot[k]
			etat = etat.listTransition[j].etatB
			j = 0
			k = k+1
			if (k == len(mot)):
				if (etat.acceptant == True):
					return 1
				else:
					return 0
		else:
			j+=1

	return 0

def verifAfnMot(mot, etat):
	# while(1):
	# 	for i in mot:
	k = 0
	j=0
	s = -1
	i = len(etat.listTransition)
	ancienEtat = etat
	ancienMot = mot
	for i in range(len(etat.listTransition)):
		mot = ancienMot
		s+= 1
		while j < len(etat.listTransition):
			# on trouve la lettre = chgt : Etat + lettreMot
			# lorsque k = len(mot) ou j = len(Transition)-> etat acceptant ?
			if ( etat.listTransition[j].verifTransition(mot[k])): #mot[k]
				etat = etat.listTransition[j].etatB
				j = s
				k = k+1
				if (k == len(mot)):
					if (etat.acceptant == True):
						return 1
					else:
						break
			else:
				j+=1

	return 0
def initialisation(automate):
	
	# On separe l'entree en deux tableaux
	auto1 = automate[:4]
	
	auto2 = []
	for a in automate[4:]:
		auto2 = auto2 + a.split()
	# init AlphaB
	auto = Automate()
	for alphaB in auto1:
		auto.recupAlphabet(alphaB)

	#init Etats
	for i in range(int(auto1[1])):
		auto.recupEtats(Etats(i))
	# nbInit = auto[2] et nbFin =  auto[3]
	auto.setInitAcceptant(auto1[2], auto1[3])

	# init Transition
	for i in range(0, len(auto2),3):
		numEtat = int(auto2[i])  # recup le 1er num qui arrive
		auto.ajoutTransition(numEtat, int(auto2[i+1]), auto2[i+2])
		
	return auto, int(auto1[2])
	
	
	
def main(automate, mot, sortie, mode):

	res = []
	tmp = 0
	auto, init = initialisation(automate)
	for i in mot:
		if (mode == '0'):
			tmp = verifAfdMot(i, auto.listEtat[init])
		
		if (mode == 1):
			print("Fonction non entierement implementee")
			#tmp = verifAfnMot(i, auto.listEtat[auto[2]])
		res.append(str(tmp) + '\n')

	sortie = open( sortie, "w")
	for i in res:
		sortie.write(i)
	sortie.close()
	return tmp

if __name__ == "__main__":
	if (len(sys.argv) != 5 ):
		print(" Utilisation : ")
		print( "nom du script + 'mode (0 ou 1)' + fichier de l'automate + fichier de mots + fichier de sortie")
		sys.exit()
	else:
		try:
			fichier = open(sys.argv[2], 'r')	
			fichierMot = open(sys.argv[3], 'r')
		except Exception as exc:
   		    raise RuntimeError("erreur ouverture fichier\n") from exc
			

		mode = sys.argv[1]
		automate = fichier.read().splitlines()
		
		mot = fichierMot.read().splitlines()
		sortie = sys.argv[4]

		fichier.close()
		fichierMot.close()

		
		main(automate, mot, sortie, mode)