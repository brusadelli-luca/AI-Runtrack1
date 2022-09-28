#retrouve le nom du pokemon dans data.txt

import re

#liste les noms des Pokemons depuis un fichier txt
fichier = open('pokemon_en.txt','rt')
texte = fichier.read()
pattern = '\n'
poke_list = re.split(pattern,texte)

#importe le texte de data.txt
fichier = open('data.txt','rt')
texte = fichier.read()

#cherche une correspondance de chaque nom de Pokemon dans data.txt
find = False
i = 0

while find == False:
    poke_name = poke_list[i]
    i = i + 1
    pattern = '[^a-zA-Z]+' + poke_name + '[^a-zA-Z]+'
    if re.findall(pattern,texte):
        print(poke_name)
        find = True