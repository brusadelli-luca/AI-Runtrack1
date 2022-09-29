#Puissance 4
import numpy as np

class Board:
    def __init__(self,i,j):
        self.plateau = np.zeros([i, j], dtype = str)
        for i1 in range(self.plateau.shape[0]):
            for j1 in range(self.plateau.shape[1]):
                self.plateau[i1,j1] = 'O'

    def play(self,n,coul):
        i = self.plateau.shape[0] - 1
        if coul == 'rouge':
            coul = 'R'
        elif coul == 'jaune':
            coul = 'J'
        else:
            print('Choisissez une couleur correcte : rouge ou jaune ?')

        while i > 0:
            if self.plateau[i,n-1] == 'O':
                self.plateau[i,n-1] = coul
                i = -1
            else:
                i = i - 1

    def Print(self):
            print(self.plateau)
jeu1 = Board(6,8)
jeu1.Print()
jeu1.play(1,'rouge')
jeu1.Print()
jeu1.play(1,'jaune')
jeu1.Print()