#puissance
def puissance(x , n):
    res = None
    if n == 0:
        res = 1
    elif n > 0:
        res = x * puissance(x , n-1)
    else:
        print("Calcul impossible")
    return res

print("x^n = ",puissance(float(input("x = ")),int(input("n = "))))