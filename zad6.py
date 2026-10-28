# Zadanie 6
def merge(lista1: list, lista2: list) -> list:
    return [x ** 3 for x in set(lista1 + lista2)]


numbs = [1, 2, 3, 4, 5, 6, 7]
numbs2 = [6, 7, 8, 9, 10]
numbs3 = merge(numbs, numbs2)

for n in numbs3:
    print(n)
