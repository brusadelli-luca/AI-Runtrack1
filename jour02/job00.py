class Personne:
    def __init__(self, nom, prenom):
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

tom = Personne("DUPONT" , "Thomas")
tom.SePresenter()

max = Personne("BLANC", "Maxime")
max.SePresenter()

tom.AfficheNom()
max.AffichePrenom()

tom.ModifNom("SOUS")
tom.SePresenter()