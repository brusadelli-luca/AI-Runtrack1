#Dames
import numpy as np

#création classe Board pour visualiser les solutions
class Board:
    def __init__(self,n):
        self.plateau = np.zeros([n, n], dtype = str)
        for i in range(n):
            for j in range(n):
                self.plateau[i,j] = 'O'
        self.taille = n

    def Print(self):
        print(self.plateau)

    def Visualiser(self,positions):
        for i in range(len(positions)):
            self.plateau[i,positions[i]] = 'X'

#fonction qui teste la possibilité d'une position en fonction de la liste des positions des dames précédentes
def possible(lgn,ls_pos):
    if len(ls_pos) < 1:
        return True
    else:    
        for i in range(len(ls_pos)):
            diff_col = len(ls_pos) - i

            if ls_pos[i] == lgn:
                return False
            elif ls_pos[i] == lgn - diff_col:
                return False    
            elif ls_pos[i] == lgn + diff_col:
                return False

        return True

#fonction de résolution en fonction de la taille du plateau
def resolution(taille,col):
    solutions = []

    if col == 1:
        for lig in range(taille):
            solutions.append([lig])

            if lig == taille - 1:
                return solutions
    else:
        solutions_i = resolution(taille,col-1)
        len_i = len(solutions_i)

        for sol in range(len_i):
            for lig in range(taille):
                if possible(lig,solutions_i[sol]) == True:
                    solutions.append(solutions_i[sol] + [lig])

            if sol == len_i - 1:
                return solutions

#fonction d'affichage du résultat
def affichage(solutions):
    if len(solutions) == 0:
        print('Il n\'y a pas de solutions.')
    else:
        print('Il y a ' + str(len(solutions)) + ' solutions.','Les solutions sont :')
        taille = len(solutions[0])
        for i in range(len(solutions)):
            resultat = Board(taille)
            resultat.Visualiser(solutions[i])
            print('\n' + 'Solution ' + str(i+1))
            resultat.Print()

n = int(input('Saisir un entier (taille du tableau) : '))
affichage(resolution(n,n))           