#% de lettre suivante pour chaque lettre dans data.txt

import re
import matplotlib.pyplot as plt

#copie tous les mots dans un liste
fichier = open('data.txt','rt')
texte = fichier.read()
pattern = '[a-zA-Z]+'
match = re.findall(pattern,texte)

#initialise les listes de comptage
lettres = []
occurrences = []

for i in range(26):
    lettres.append(chr(65 + i))
    occurrences.append([])
    for j in range(26):
        occurrences[i].append(0)

#Boucle sur tous les mots listés
for i in range(len(match)):

    #Boucle sur les lettres d'un mot sauf la dernière
    for j in range(len(match[i])-1):
        
        ord_lettre = ord(match[i][j].lower())-97

        #Boucle sur les lettres suivantes dans le mot
        for k in range(j + 1,len(match[i])):

            ord_lettre_suiv = ord(match[i][k].lower())-97
            occurrences[ord_lettre][ord_lettre_suiv] = occurrences[ord_lettre][ord_lettre_suiv] + 1

#Conversion des occurrences en %
for i in range(26):
    total = sum(occurrences[i])

    for j in range(len(occurrences)):
        if sum(occurrences[i]) != 0:
            occurrences[i][j] = occurrences[i][j] / total * 100

#Affichage
fig, ax = plt.subplots()

for i in range(26):
    ax.plot(lettres,occurrences[i],label=lettres[i])

ax.legend()
ax.set_ylabel('Apparition (%)')
ax.set_title('Occurrences des lettres suivantes dans data.txt')

plt.show()