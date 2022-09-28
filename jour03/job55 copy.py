#% de nombres de mots par phrase dans data.txt

import re

fichier = open('data.txt','rt')
texte = fichier.read()
pattern = '\.'
match = re.split(pattern,texte)
phrases = match

nombre_mots =[]
pattern = '[a-zA-Z]+'
gde_phrase = 0

occurrences = []

for i in range(len(phrases)):
    if len(re.findall(pattern,phrases[i])) > gde_phrase:
        gde_phrase = len(re.findall(pattern,phrases[i]))
    nombre_mots.append(len(re.findall(pattern,phrases[i])))
    
for i in range(gde_phrase):
    occurrences.append(0)

for i in range(len(phrases)):
    occurrences[nombre_mots[i]-1] = occurrences[nombre_mots[i]-1] + 1

#Conversion des occurrences en %
for i in range(len(occurrences)):
    occurrences[i] = occurrences[i] / len(phrases)

fichier = open("taille_phrase.txt","w")
fichier.write(str(occurrences))