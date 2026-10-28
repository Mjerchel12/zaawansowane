# Zadanie 2
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


class Employee:

    def __init__(self, first_name, last_name, hire_date,
                 birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        string = self.first_name
        string = string + " " + self.last_name
        string = string + ", zatrudniony/a: " + str(self.hire_date)
        string = string + ", urodzony/a: " + str(self.birth_date)
        string = string + ". Z: " + self.city
        string = string + " " + self.street
        string = string + " " + self.zip_code

        return string + " " + ". Tel: " + str(self.phone)


class Book:

    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        string = "Jest w " + str(self.library)
        string = string + ". Wydana w: " + str(self.publication_date)
        string = string + ". Autor: " + self.author_name
        string = string + " " + self.author_surname
        return string + ". Ilość stron: " + str(self.number_of_pages)


class Order:

    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        bookstring = ""
        for book in self.books:
            bookstring = bookstring + ", " + str(book) + "\n"

        string = "Zamówienie ogarniane przez " + str(self.employee)
        string = string + " dla " + self.student
        string = string + "." + bookstring
        return string + ". Zamówione w: " + self.order_date


aleksandryjska = Library("Alexandria",
                         "Ptolemeusza 2", "67-420", "20-22", 720898111)
inna = Library("Inne miasto",
               "Kogoś innego 1", "69-240", "12-22", 720898111)

kapital = Book(aleksandryjska,
               1893, "Karl", "Marx", 2600)
encykliki = Book(aleksandryjska,
                 1979, "Jan", "Paweł II", 2137)
emberdark = Book(aleksandryjska,
                 2137, "Brandon", "Sanderson", 900)
odyseja = Book(inna,
               2026, "Christopher", "Nolan", 20)
innaksiazka = Book(inna,
                   20, "Inny", "Autor", 67)

hoxha = Employee("Enver", "Hoxha", 1985, 1908,
                 "Gjirokaster", "Albańska", "66-666", 720898111)
sankara = Employee("Thomas", "Sankara", 1987, 1949,
                   "Wagadugu", "Bazowana", "67-676", 720898111)
hochiminh = Employee("Ho", "Chi Minh", 1969, 1890,
                     "Nghe An", "Wietkongu", "77-777", 720898111)

lassale = "Ferdinand Lassale"
mamdani = "Zohran Mamdani"

lassaleOrder = Order(hoxha, lassale,
                     [kapital, encykliki], "21.10.2026")
mamdaniOrder = Order(sankara, mamdani,
                     [odyseja, innaksiazka], "21.10.2026")

print(lassaleOrder)
print(mamdaniOrder)
