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