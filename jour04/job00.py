#factorielle
def factorielle(n):
    res = None
    if n == 0:
        res = 1
    elif n > 0:
        res = n * factorielle(n-1)
    else:
        print("Calcul impossible")
    return res

print("n! = ",factorielle(int(input("n = "))))