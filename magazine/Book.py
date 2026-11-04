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