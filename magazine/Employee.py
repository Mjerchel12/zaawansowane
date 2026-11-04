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