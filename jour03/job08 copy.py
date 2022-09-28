#% d'apparition de chaque taille de mot dans data.txt
import re

fichier = open('data.txt','rt')
texte = fichier.read()
pattern = '[a-zA-Z]+'
match = re.findall(pattern,texte)
cpt = []
taille = []
mx = 0
for i in range(len(match)):
    if len(match[i]) > mx:
        mx = len(match[i])
for i in range(mx):
    cpt.append(0)
    taille.append(i+1)
for i in range(len(match)):
    cpt[len(match[i])-1] = cpt[len(match[i])-1] + 1
for i in range(len(cpt)):
    cpt[i] = cpt[i]/len(match)

fichier = open("mots.txt","w")
fichier.write(str(taille))
fichier.write(str(cpt))