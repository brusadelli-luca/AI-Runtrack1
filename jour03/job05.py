#% d'apparition de chaque lettre de data.txt

import re
import matplotlib.pyplot as plt

fichier = open('data.txt','rt')
texte = fichier.read()
lettres = []
occurrences = []
total_lettres = 0
for i in range(26):
    pattern = '[' + chr(65 + i) + chr(97 + i) + ']'
    matches = re.findall(pattern,texte)
    lettres.append(chr(65 + i))
    occurrences.append(len(matches))
    total_lettres = total_lettres + occurrences[i]

for i in range(26):
    occurrences[i] = occurrences[i]/total_lettres*100

fig, ax = plt.subplots()
ax.bar(lettres,occurrences)
ax.set_ylabel('Apparition (%)')
ax.set_title('Occurrences des lettres dans data.txt')

plt.show()