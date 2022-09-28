#% de phrases par taille dans data.txt

import re
import matplotlib.pyplot as plt

#copie les phrases dans une liste
fichier = open('data.txt','rt')
texte = fichier.read()
pattern = '\.'
match = re.split(pattern,texte)
phrases = match

#compte le nombre de mot par phrase dans une liste et cherche la phrase la plus longue
nombre_mots =[]
pattern = '[a-zA-Z]+'
gde_phrase = 0

occurrences = []

for i in range(len(phrases)):
    if len(re.findall(pattern,phrases[i])) > gde_phrase:
        gde_phrase = len(re.findall(pattern,phrases[i]))
    nombre_mots.append(len(re.findall(pattern,phrases[i])))

#compte les occurences de chaque taille de phrase
for i in range(gde_phrase):
    occurrences.append(0)

for i in range(len(phrases)):
    occurrences[nombre_mots[i]-1] = occurrences[nombre_mots[i]-1] + 1

#Conversion des occurrences en %
for i in range(len(occurrences)):
    occurrences[i] = occurrences[i] / len(phrases) * 100

#Affichage
fig, ax = plt.subplots()

ax.bar(range(gde_phrase),occurrences)

ax.set_ylabel('Apparition (%)')
ax.set_title('Longueurs de phrases en nombre de mots dans data.txt')

plt.show()