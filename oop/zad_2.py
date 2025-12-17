from typing import List


class Library:
    def __init__(
        self, city: str,
            street: str,
            zip_code: str,
            open_hours: str,
            phone: str
    ):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka: {self.city}, {self.street}, {self.zip_code}"


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: str,
        birth_date: str,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name}"


class Student:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"


class Book:
    def __init__(
        self,
        library: Library,
        publication_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Książka: {self.author_name} {self.author_surname}, "
            f"{self.number_of_pages} stron, {self.library}"
        )


class Order:
    def __init__(
        self,
        employee: Employee,
        student: Student,
        books: List[Book],
        order_date: str,
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n".join(str(book) for book in self.books)
        return (
            f"Zamówienie z dnia {self.order_date}\n"
            f"{self.employee}\n"
            f"{self.student}\n"
            f"Książki:\n{books_str}\n"
            f"{'-' * 40}"
        )


library1 = Library("Warszawa", "Kwiatowa 1", "00-001", "8-16", "123456789")
library2 = Library("Kraków", "Długa 5", "30-001", "9-17", "987654321")

books = [
    Book(library1, "2020", "Adam", "Mickiewicz", 300),
    Book(library1, "2018", "Henryk", "Sienkiewicz", 400),
    Book(library2, "2021", "Bolesław", "Prus", 350),
    Book(library2, "2019", "Maria", "Konopnicka", 280),
    Book(library2, "2022", "Juliusz", "Słowacki", 320),
]

employee1 = Employee("Jan",
                     "Nowak",
                     "2020",
                     "1990",
                     "Warszawa",
                     "A",
                     "00-001",
                     "111")
employee2 = Employee("Anna",
                     "Kowalska",
                     "2019",
                     "1988",
                     "Kraków",
                     "B",
                     "30-001",
                     "222")
employee3 = Employee("Piotr",
                     "Zieliński",
                     "2021",
                     "1995",
                     "Kraków",
                     "C",
                     "30-002",
                     "333")

student1 = Student("Ola")
student2 = Student("Tomek")
student3 = Student("Asia")

order1 = Order(employee1, student1, books[:3], "2024-01-10")
order2 = Order(employee2, student2, books[3:], "2024-01-11")

print(order1)
print(order2)
