# Zadanie 5
def isinlist(list, num):
    return num in list


list = [1, 2, 3]
if isinlist(list, 2):
    print("Jest")
else:
    print("Nie jest")

if isinlist(list, 6):
    print("Jest")
else:
    print("Nie jest")
