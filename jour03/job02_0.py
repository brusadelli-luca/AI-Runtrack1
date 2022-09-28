import re
fichier = open('../data.txt','rt')
texte = fichier.read()
pattern = '\s'
wrds = re.split(pattern,texte)
print(len(wrds))