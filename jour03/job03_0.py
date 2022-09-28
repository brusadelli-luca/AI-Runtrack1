import re
taille = input('Quelle est la taille de mot recherchée ? : ')
fichier = open('../data.txt','rt')
texte = fichier.read()
#pattern = '\s'
#wrds = re.split(pattern,texte)
#print(len(wrds))
pattern = '[a-zA-Z]{' + taille + '}\s'
matches = re.findall(pattern,texte)
print(int(len(matches)+1),matches)