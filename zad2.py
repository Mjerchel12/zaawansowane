from magazine.Library import Library
from magazine.Book import Book
from magazine.Employee import Employee
from magazine.Order import Order

# Zadanie 2
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
