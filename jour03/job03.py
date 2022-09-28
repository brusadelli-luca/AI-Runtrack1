#demande de renseigner un nombre entier et compte le nombre de mots de la taille renseignée qui se trouvent dans data.txt

import re
fichier = open('data.txt','rt')
texte = fichier.read()
pattern = '[a-zA-Z]+'
match = re.findall(pattern,texte)
cpt = 0
taille = int(input('Quelle est la taille de mot recherchée ? : '))
for i in range (len(match)):
    if len(match[i]) == taille:
        cpt = cpt + 1
print(cpt)