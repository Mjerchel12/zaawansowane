# Zadanie 3
class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return self.area + " " + str(self.rooms) + " " + self.price + " " + self.address

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return self.area + " " + str(self.rooms) + " " + self.price + " " + self.address + " " + self.plot

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return self.area + " " + str(self.rooms) + " " + self.price + " " + self.address + " " + str(self.floor)

dom = House("2cm2", 1, "213,7K franków szwajcarskich", "Świdra 2", "3cm2")
płaski = Flat("2mm2", 2, "67K dolarów namibijskich", "Tuska 1", 1987)

print(dom)
print(płaski)