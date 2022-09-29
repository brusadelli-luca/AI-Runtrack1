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

vh = Auteur('HUGO', 'Victor')
vh.SePresenter()
vh.listerOeuvre()
livre1 = vh.ecrireUnLivre('Vingt Mille Lieux Sous Les Mers')
print(livre1.titre)
vh.listerOeuvre()