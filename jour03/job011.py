#parcourt domains.xml et compte le nombre d'extensions de domaines

import re

fichier = open('domains.xml','rt')
texte = fichier.read()

#obtient une liste avec les extensions
pattern = '<column name="domain">'
matches = re.split(pattern,texte)

pattern = '</column>'

for i in range(1,len(matches)):

    matches[i] = re.split(pattern,matches[i])[0]
    lg = len(re.split('\.',matches[i]))
    matches[i] = re.split('\.',matches[i])[lg-1]

matches.remove(matches[0])

#compte les extensions par type
extensions =[]

while len(matches)>0:
    extensions.append([matches[0], len(re.findall(matches[0],str(matches)))])

    for i in range(extensions[len(extensions)-1][1]):
        matches.remove(extensions[len(extensions)-1][0])
    
    print(matches)

print(extensions)