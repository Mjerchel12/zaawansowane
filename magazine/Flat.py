from magazine.Property import Property

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        string = self.area
        string = string + " " + str(self.rooms)
        string = string + " " + self.price
        string = string + " " + self.address
        return string + " " + str(self.floor)