# Zadanie 6
from magazine.utility import merge

numbs = [1, 2, 3, 4, 5, 6, 7]
numbs2 = [6, 7, 8, 9, 10]
numbs3 = merge(numbs, numbs2)

for n in numbs3:
    print(n)
