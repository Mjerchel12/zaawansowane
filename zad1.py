# Zadanie 1
class Student:

    def __init__(self, name, marx):
        self.name = name
        self.marx = marx

    def is_passed(self):
        sum = 0
        quant = 0
        for mark in self.marx:
            sum= sum+mark
            quant=quant+1

        print(sum)
        print(quant)
        print(sum/quant)
        
        if sum/quant > 50:
            return True
        else:
            return False

Lenin = Student("Vladimir Lenin", [1,2,3])

print(Lenin.is_passed())

Xiaoping = Student("Xiaopoing Deng", [50,60,70])

print(Xiaoping.is_passed())