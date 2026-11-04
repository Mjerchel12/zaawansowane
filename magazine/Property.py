class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        string = self.area
        string = string + " " + str(self.rooms)
        string = string + " " + self.price
        return string + " " + self.address