def mot_suivant(mot):
    liste_mot = list(mot)
    lg_mot = len(mot)
    liste_mot_ord = []
    
    for i in range(lg_mot):
        liste_mot_ord.append(ord(liste_mot[i]))
    i = lg_mot - 1 - 1
    min_diff = 26
    
    while i >= 0:
        lettre1 = liste_mot_ord[i]
        
        for j in range(i + 1, lg_mot):
            lettre2 = liste_mot_ord[j]
            
            if lettre1 < lettre2 and min_diff > lettre2 - lettre1:
                min_diff = lettre2 - lettre1
                tmp_ind = j
        
        if min_diff < 26:
            tmp_cont = liste_mot_ord[i]
            liste_mot_ord[i] = liste_mot_ord[tmp_ind]
            liste_mot_ord[tmp_ind] = tmp_cont

            for j in range(i + 1, lg_mot):
                
                for k in range(j + 1, lg_mot):
                    
                    if liste_mot_ord[k] < liste_mot_ord[j]:
                        tmp_cont = liste_mot_ord[j]
                        liste_mot_ord[j] = liste_mot_ord[k]
                        liste_mot_ord[k] = tmp_cont
            i = -1
        
        else:
            i = i -1
    mot_suiv = ""
    
    for i in range(lg_mot):
        mot_suiv = mot_suiv + chr(liste_mot_ord[i])
        print("Le mot suivant est : " + mot_suiv)
        
mot_suivant(input("Saisissez un mot : "))