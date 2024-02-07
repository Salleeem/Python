# Calculadora de equações de segundo grau

import math


def calcular(a, b, c):
    bhaskara = b**2 - 4 * a * c

    if bhaskara > 0:
        raiz1 = (-b + math.sqrt(bhaskara)) / (2 * a)
        raiz2 = (-b - math.sqrt(bhaskara)) / (2 * a)
        return raiz1, raiz2
    elif bhaskara == 0:
        raiz = -b / (2 * a)
        return raiz, raiz
    else:
        parte_real = -b / (2 * a)
        parte_imaginaria = math.sqrt(abs(bhaskara)) / (2 * a)
        return (parte_real, parte_imaginaria), (parte_real, -parte_imaginaria)


a = float(input("Digite o'a': "))
b = float(input("Digite o'b': "))
c = float(input("Digite o'c': "))

raizes = calcular(a, b, c)

if isinstance(raizes[0], tuple):
    print("As raízes são complexas:")
    for raiz in raizes:
        print(raiz[0], "+", raiz[1], "i")
else:
    print("As raízes são:", raizes)
