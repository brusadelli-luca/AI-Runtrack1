#Livres

class Livre:
    def __init__(self,titre):
        self.titre = titre
        #Auteur ? 
    def Print(self):
        print("Le titre du livre est : ", self.titre)

class Personne:
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom
    def SePresenter(self):
        print(self.nom, self.prenom)
    def AfficheNom(self):
        print("Le nom est : ", self.nom)
    def AffichePrenom(self):
        print("Le prénom est : ", self.prenom)
    def ModifNom(self,nom):
        self.nom = nom
        print("Le nom a été modifié. Nouveau nom : ", self.nom)
    def ModifPrenom(self,prenom):
        self.prenom = prenom
        print("Le prénom a été modifié. Nouveau prénom : ", self.prenom)

class Auteur(Personne):
    def __init__(self,nom,prenom):
        super().__init__(nom,prenom)
        self.oeuvre = []
    def listerOeuvre(self):
        print("Liste des oeuvres de", self.nom, self.prenom,self.oeuvre)
    def ecrireUnLivre(self,titre):
        self.oeuvre.append(titre)
        return Livre(titre)

class Client(Personne):
    def __init__(self,nom,prenom):
        super().__init__(nom,prenom)
        self.collection = []
    def inventaire(self):
        print("Collection de", self.nom, self.prenom, self.collection)

class Bibliotheque:
    def __init__(self):
        self.nom = ''
        self.catalogue = []
    
    def acheterLivre(self,auteur,nom,qte):
        for titre in auteur.oeuvre:
            if nom == titre:
                self.catalogue.append([nom,qte])

    def inventaire(self):
        print("Catalogue le la bibliothèque",self.catalogue)

    def louer(self,client,nom):
        for i in range(len(self.catalogue)):
            if self.catalogue[i][0] == nom and self.catalogue[i][1] > 0:
                self.catalogue[i][1] = self.catalogue[i][1] - 1
                client.collection.append(nom)

    def rendreLivres(self,client):
        for i in range(len(client.collection)):
            for j in range(len(self.catalogue)):
                if client.collection[i] == self.catalogue[j][0]:
                    self.catalogue[j][1] = self.catalogue[j][1] + 1
        client.collection = []

bib1 = Bibliotheque()
vh = Auteur('HUGO','Victor')
jv = Auteur('VERNE','Jules')

bib1.acheterLivre(vh,'20 Mille Lieues',10)
bib1.inventaire()

vh.listerOeuvre()
vh.ecrireUnLivre(('20 Mille Lieues'))
vh.listerOeuvre()

jv.ecrireUnLivre("Les Fables")

bib1.acheterLivre(vh,'20 Mille Lieues',10)
bib1.acheterLivre(jv,'Les Fables', 2)
bib1.inventaire()

tom = Client('Moulin', 'Thomas')
bib1.louer(tom, '20 Mille Lieues')
tom.inventaire()
bib1.inventaire()

bib1.rendreLivres(tom)
tom.inventaire()
bib1.inventaire()