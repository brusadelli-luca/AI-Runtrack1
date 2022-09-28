#parcourt data.txt et compte le nombre de mots (sans caractère spéciaux)

import re
fichier = open('data.txt','rt')
texte = fichier.read()
pattern = '[a-zA-Z]+'
match = re.findall(pattern,texte)
print(len(match))