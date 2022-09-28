#retrouve le nom du pokemon dans data.txt

import re
fichier = open('pokemon_en.txt','rt')
texte = fichier.read()
pattern = '\n'
poke_list = re.split(pattern,texte)

fichier = open('data.txt','rt')
texte = fichier.read()
pattern = '[a-zA-Z]+'
liste_mots = re.findall(pattern,texte)

find = False
i = 0

while find == False:
    poke_name = poke_list[i]
    i = i + 1
    j = 0
    while find == False and j < len(liste_mots):
        mot = liste_mots[j]
        j = j + 1  
        if poke_name == mot:
            print(poke_name)
            find = True