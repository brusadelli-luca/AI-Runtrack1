def draw_rectangle(width, height):
    for i in range(int(height)):
        if i == 0 or i == (int(height) - 1):
            ligne = "|"
            for j in range(int(width)-2):
                ligne = ligne + "-"
            ligne = ligne + "|" 
        else:
            ligne = "|"
            for j in range(int(width)-2):
                ligne = ligne + " "
            ligne = ligne + "|" 
        print(ligne)
draw_rectangle(input("Largeur ? : "), input("Hauteur ? : "))