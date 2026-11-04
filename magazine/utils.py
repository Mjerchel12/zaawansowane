def print_names(list):
    for name in list:
        print(name)

def multiplyfor(list):
    new_list = []
    for num in list:
        new_list.append(num * 2)
    return new_list

def multiplylist(list):
    return [num*2 for num in list]

def showeven(list):
    for n in list:
        if n % 2 == 0:
            print(n)

def showsecond(list):
    cycle = 0
    for n in list:
        cycle += 1
        if cycle % 2 == 0:
            print(n)