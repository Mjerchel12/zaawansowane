# Zadanie 5
from magazine.utility import isinlist

list = [1, 2, 3]
if isinlist(list, 2):
    print("Jest")
else:
    print("Nie jest")

if isinlist(list, 6):
    print("Jest")
else:
    print("Nie jest")
