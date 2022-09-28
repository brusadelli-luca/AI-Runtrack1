def ordonner(nb1,nb2,nb3,nb4,nb5):
    liste = [int(nb1), int(nb2), int(nb3), int(nb4), int(nb5)]
    tmp = 0
    for i in range(len(liste)-1):
        for j in range(i + 1, len(liste)):
            if liste[j] < liste[i]:
                tmp = liste[i]
                liste[i] = liste[j]
                liste[j] = tmp
    for i in range(5):
        print(liste[i])
ordonner(input("Nombre 1 : "), input("Nombre 2 : "), input("Nombre 3 : "), input("Nombre 4 : "), input("Nombre 5 : "))