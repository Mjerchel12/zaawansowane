class Student:

    def __init__(self, name, marx):
        self.name = name
        self.marx = marx

    def is_passed(self):
        sum = 0
        quant = 0
        for mark in self.marx:
            sum = sum + mark
            quant = quant + 1

        print(sum)
        print(quant)
        print(sum/quant)

        if sum/quant > 50:
            return True
        else:
            return False