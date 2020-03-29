import random

class Monopoly:
    def __init__(self,banque=0):
        self.liste_cases=[case_0,case_1,case_2,case_3,case_4,case_5,case_6,case_7,case_8,case_9,case_10,case_11,case_12,case_13,
                          case_14,case_15,case_16,case_17,case_18,case_19,case_20,case_21,case_22,case_23,case_24,
                          case_25,case_26,case_27,case_28,case_29,case_30,case_31,case_32]
        self.liste_joueurs=[]
        self.banque=banque
    def add_joueurs(self,joueur):
        self.liste_joueurs.append(joueur)
    def debut_partie(self):
        print("La partie commence...")
        NewList=[]
        for i in range(len(self.liste_joueurs)):
            rnd=random.choice(self.liste_joueurs)
            self.liste_joueurs.remove(rnd)
            NewList.append(rnd)
        print("Ordre des Joueurs :")
        for k in range(0,len(NewList)):
            print(NewList[k].name)
        return NewList

    def fin_de_tour(self):
        a=input("Est-ce la fin du tour ?")

    def partie(self):
        ListeDeJoueur=Monopoly.debut_partie(self)
        avancement=random.randint(2,12)
        print(ListeDeJoueur[0].name,"avance de",avancement)
        c1=self.liste_cases[avancement]
        j1=ListeDeJoueur[0]
        print(j1.name,",vous êtes tombé sur la case :",c1.nom)
        if type(c1)==Terrain:
            print("Votre solde est de :",j1.compte)
            demande=input("Voulez vous acheter cette case ?")
            if demande=="oui":
                j1.compte-=c1.prix
                j1.liste_de_cartes.append(c1)
                c1.etat=1
            j1.position=self.liste_cases.index(c1)
        elif type(c1)==Gare:
            print("Votre solde est de :",j1.compte)
            a=input("Voulez acheter cette case ?")
            if a=="oui":
                j1.compte-=c1.prix
                j1.liste_de_cartes.append(c1)
                j1.nb_gares+=1
                c1.etat=1
            j1.position=self.liste_cases.index(c1)
        elif type(c1)==Malus:
            j1.compte-=c1.malus
            self.banque+=c1.malus
            j1.position=self.liste_cases.index(c1)
            print("Vous devez payer",c1.malus,"€")
        elif type(c1)==Bonus:
            print("Vous avez recu",c1.bonus,"€")
            j1.compte+=c1.bonus
            print("Votre solde est de :",j1.compte)
            j1.position=self.liste_cases.index(c1)
        elif type(c1)==Compagnie:
            print("Votre solde est de :",j1.compte)
            a=input("Voulez acheter cette case ?")
            if a=="oui":
                j1.compte-=c1.prix
                j1.liste_de_cartes.append(c1)
                j1.nb_compagnies+=1
                c1.etat=1
        Monopoly.fin_de_tour(self)

        fin=False
        cursorprec=0
        while fin==False:
            index=ListeDeJoueur.index(j1)
            newindex=index+1
            if ListeDeJoueur[newindex]!=ListeDeJoueur[-1]:
                j_actif=ListeDeJoueur[newindex]
            else:
                j_actif=ListeDeJoueur[newindex]
                g=ListeDeJoueur[-1]
                ListeDeJoueur.remove(g)
                ListeDeJoueur.insert(0,g)
            print("Au tour de :",j_actif.name)
            avancement=random.randint(2,12)
            print(j_actif.name,"avance de",avancement)
            j_actif.position+=avancement
            if j_actif.position>32:
                j_actif.position=cursorprec-32+avancement
                case_active=self.liste_cases[j_actif.position-1]
                if case_active.nom!="Départ":
                    j_actif.compte+=200
                    print("Vous êtes passés par la case départ et avez reçu 200€")
                    print("Votre solde est de :",j_actif.compte)
            elif j_actif.position >= 20:
                cursorprec=j_actif.position
                case_active=self.liste_cases[j_actif.position]
            else:
                case_active=self.liste_cases[j_actif.position]
            print(j_actif.name,", vous êtes tombé sur la case :",case_active.nom)
            if type(case_active)==Malus:
                print("Vous devez payer",case_active.malus,"€")
                j_actif.compte-=case_active.malus
                self.banque+=case_active.malus
            elif type(case_active)==Gare:
                if case_active.etat==0:
                    print("Votre solde est de :",j_actif.compte)
                    a=input("Voulez acheter cette case ?")
                    if a=="oui":
                        j_actif.compte-=case_active.prix
                        j_actif.liste_de_cartes.append(case_active)
                        j_actif.nb_gares+=1
                        case_active.etat=1
                else:
                    for i in ListeDeJoueur:
                        for k in i.liste_de_cartes:
                            if k==case_active:
                                j_actif.compte-=case_active.loyer*i.nb_gares
                                i.compte+=case_active.loyer*i.nb_gares
                                print("Cette case appartient à :",i.nom,"Vous lui devez :",case_active.loyer*i.nb_gares)
                                print("Votre solde est de :",j_actif.compte)
            elif type(case_active)==Terrain:
                if case_active.etat==0:
                    print("Votre solde est de :",j_actif.compte)
                    a=input("Voulez acheter cette case ?")
                    if a=="oui":
                        j_actif.compte-=case_active.prix
                        j_actif.liste_de_cartes.append(case_active)
                        case_active.etat=1
                else:
                    for i in ListeDeJoueur:
                        for k in i.liste_de_cartes:
                            if k==case_active:
                                j_actif.compte-=case_active.loyer
                                i.compte+=case_active.loyer
                                print("Cette case appartient à :",i.nom,"Vous lui devez :",case_active.loyer)
                                print("Votre solde est de :",j_actif.compte)
            elif type(case_active)==Compagnie:
                if case_active.etat==0:
                    print("Votre solde est de :",j_actif.compte)
                    a=input("Voulez acheter cette case ?")
                    if a=="oui":
                        j_actif.compte-=case_active.prix
                        j_actif.liste_de_cartes.append(case_active)
                        j_actif.nb_compagnies+=1
                        case_active.etat=1
                else:
                    for i in ListeDeJoueur:
                        for k in i.liste_de_cartes:
                            if k==case_active:
                                if i.nb_compagnies==1:
                                    j_actif.compte-=4*avancement
                                    i.compte+=4*avancement
                                    print("Cette case appartient à :",i.nom,"Vous lui devez :",4*avancement)
                                    print("Votre solde est de :",j_actif.compte)
                                else:
                                    j_actif.compte-=10*avancement
                                    i.compte+=10*avancement
                                    print("Cette case appartient à :",i.nom,"Vous lui devez :",10*avancement)
                                    print("Votre solde est de :",j_actif.compte)
            elif type(case_active)==Bonus:
                if case_active.nom=="parc gratuit":
                    print("Vous avez recu",self.banque,"€")
                    j_actif.compte+=self.banque
                    print("Votre solde est de :",j_actif.compte)
                    self.banque=0
                else:
                    print("Vous avez recu",case_active.bonus,"€")
                    j_actif.compte+=case_active.bonus
                    print("Votre solde est de :",j_actif.compte)
            Monopoly.fin_de_tour(self)
            j1=j_actif

class Joueur:
    def __init__(self,name,compte,position=0,nb_gares=0,nb_compagnies=0):
        self.name=name
        self.position=position
        self.compte=compte
        self.liste_de_cartes=[]
        self.nb_gares=nb_gares
        self.nb_compagnies=nb_compagnies

class Case:
    def __init__(self,nom,etat=0):
        self.nom=nom
        self.etat=etat
class Terrain(Case):
    def __init__(self,nom,prix,loyer):
        Case.__init__(self,nom)
        self.prix=prix
        self.loyer=loyer

class Gare(Case):
    def __init__(self,nom,prix,loyer):
        Case.__init__(self,nom)
        self.prix=prix
        self.loyer=loyer

class Malus(Case):
    def __init__(self,nom,malus):
        Case.__init__(self,nom)
        self.malus=malus

class Bonus(Case):
    def __init__(self,nom,bonus):
        Case.__init__(self,nom)
        self.bonus=bonus

class Compagnie(Case):
    def __init__(self,nom,prix):
        Case.__init__(self,nom)
        self.prix=prix



case_0=Bonus("Départ",200)
case_1=Terrain("Boulevard de Belleville",60,2)
case_2=Terrain("Rue Lecourbe",60,4)
case_3=Malus("Impôt sur le revenu",200)
case_4=Gare("Gare Montparnasse",200,50)
case_5=Terrain("Rue de Vaugirard",100,6)
case_6=Terrain("Rue de Courcelles",100,6)
case_7=Terrain("Avenue de la Republique",120,8)
case_8=Bonus("case de remplacement",200)
case_9=Terrain("Boulevard de la Vilette",140,10)
case_10=Terrain("Avenue de Neuilly",140,10)
case_11=Compagnie("Compagnie de distribution d'électricité",150)
case_12=Terrain("Rue de Paradis",160,12)
case_13=Terrain("Gare de Lyon",200,50)
case_14=Terrain("Avenue Mozard",180,14)
case_15=Terrain("Boulevard Saint-Michel",180,14)
case_16=Terrain("Place Pigalle",200,16)
case_17=Bonus("parc gratuit",100)
case_18=Terrain("Avenue Matignon",220,18)
case_19=Terrain("Boulevard Malherbes",220,18)
case_20=Terrain("Avenue Henri-Martin",240,20)
case_21=Gare("Gare du Nord",200,50)
case_22=Terrain("Faubourg Saint Honoré",260,22)
case_23=Terrain("Place de la Bourse",260,22)
case_24=Compagnie("Compagnie de distribution des eaux",150)
case_25=Terrain("Rue la Fayette",280,24)
case_26=Terrain("Avenue de Breteuil",300,26)
case_27=Terrain("Avenue Foch",300,26)
case_28=Terrain("Boulevard des Capucines",320,28)
case_29=Gare("Gare Saint-Lazard",200,50)
case_30=Terrain("Avenue des Champs-Elysées",350,35)
case_31=Malus("Taxe de Luxe",100)
case_32=Terrain("Rue de la Paix",400,50)

