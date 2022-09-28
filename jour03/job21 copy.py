#% de lettre suivante pour chaque lettre dans data.txt

import re

fichier = open('data.txt','rt')
texte = fichier.read()
pattern = '[a-zA-Z]+'
match = re.findall(pattern,texte)
lettres = []
occurrences = []

for i in range(26):
    lettres.append(chr(65 + i))
    occurrences.append([])
    for j in range(26):
        occurrences[i].append(0)

#Boucle sur tous les mots
for i in range(len(match)):

    #Boucle sur les lettres d'un mot sauf la derniere
    for j in range(len(match[i])-1):
        
        ord_lettre = ord(match[i][j].lower())-97

        #Boucle sur les lettres suivantes
        for k in range(j + 1,len(match[i])):

            ord_lettre_suiv = ord(match[i][k].lower())-97
            occurrences[ord_lettre][ord_lettre_suiv] = occurrences[ord_lettre][ord_lettre_suiv] + 1

#Conversion des occurrences en %
for i in range(26):
    total = sum(occurrences[i])

    for j in range(len(occurrences)):
        if sum(occurrences[i]) != 0:
            occurrences[i][j] = occurrences[i][j] / total

fichier = open("suivante.txt","w")
for i in range(26):
    fichier.write(str(lettres[i]))
    fichier.write(str(occurrences[i]))
    fichier.write("\n")