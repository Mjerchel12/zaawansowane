class Library:

    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        string = "Biblioteka w " + self.city
        string = string + " na ulicy " + self.street
        string = string + ", " + self.zip_code
        string = string + ". Otwarta: " + self.open_hours
        return string + "Tel: " + str(self.phone)