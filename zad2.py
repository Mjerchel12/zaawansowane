# Zadanie 2bi
def multiplyfor(list):
    new_list = []
    for num in list:
        new_list.append(num * 2)
    return new_list


print("NUMERKI")
numbs = [1, 2, 3, 4, 5]
numbs = multiplyfor(numbs)
for n in numbs:
    print(n)
print("\n")
