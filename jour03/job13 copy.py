#% de présence de chaque lettre en début de mot dans data.txt
import re

fichier = open('data.txt','rt')
texte = fichier.read()
pattern = '[a-zA-Z]+'
match = re.findall(pattern,texte)
lettres = []
occurrences = []

for i in range(26):
    lettres.append(chr(65 + i))
    occurrences.append(0)

for i in range(len(match)):
    if ord(match[i][0]) >= 65 and ord(match[i][0]) < (65 + 26):
        occurrences[ord(match[i][0])-65] = occurrences[ord(match[i][0])-65] + 1
    elif ord(match[i][0]) >= 97 and ord(match[i][0]) < (97 + 26):
        occurrences[ord(match[i][0])-97] = occurrences[ord(match[i][0])-97] + 1

for i in range(len(occurrences)):
    occurrences[i] = occurrences[i] / len(match)

fichier = open("debut.txt","w")
fichier.write(str(lettres))
fichier.write(str(occurrences))