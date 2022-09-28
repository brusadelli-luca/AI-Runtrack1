def draw_triangle(hgt):
    height = int(hgt)
    width = height * 2
    avant = width//2-1
    for i in range(height):
        if i != height-1:
            ligne = " "
            for j in range(avant-1):
                ligne = ligne + " "
            ligne = ligne + "/"
            for j in range(i):
                ligne = ligne + "  "
            ligne = ligne + "\\"
            avant = avant - 1
        else:
            ligne = "/"
            for j in range(width-2):
                ligne = ligne + "_"
            ligne = ligne + "\\"
        print(ligne)
draw_triangle(input("Hauteur ? : "))