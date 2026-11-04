from magazine.Property import Property

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        string = self.area
        string = string + " " + str(self.rooms)
        string = string + " " + self.price
        string = string + " " + self.address
        return string + " " + self.plot