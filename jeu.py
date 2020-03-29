
from test2 import *

#Configuration de la partie
monopoly=Monopoly()
Joueur1=Joueur("Guillaume",1500)
Joueur2=Joueur("Armando",1500)
monopoly.add_joueurs(Joueur1)
monopoly.add_joueurs(Joueur2)
#monopoly.debut_partie()

#Lancement de la partie
print("-------------")
monopoly.partie()


