#renseigner chaine de caractères et écrire dans output.txt

chaine = input("Veuillez taper un texte : ")
fichier = open("output.txt","w")
fichier.write(chaine)