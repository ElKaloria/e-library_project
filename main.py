import itertools
import json


class Book:
    _id = itertools.count(1)

    def __init__(self, title, author, year, status, id = None):
        self.id = id if id else self._id.__next__()
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return f"Книга с номером {self.id}, {self.title} автор {self.author} ({self.year})"


def write_book(book):
    with open("library.json", "w+", encoding="cp1251") as file:
        books = json.load(file)
        if books is None:
            books = []
        books.append(book.__dict__)
        json.dump(books, file, ensure_ascii=False, indent=4)


def print_all_books():
    with open("library.json", "r", encoding="cp1251") as file:
        books = json.load(file)
        for book in books:
            print(Book(**book))


def change_book_status(book_id, new_status):
    with open("library.json", "r", encoding="cp1251") as file:
        books = json.load(file)
        for book in books:
            if book["id"] == book_id:
                book["status"] = new_status
    with open("library.json", "w", encoding="cp1251") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    # book = Book("The Catcher in the Rye", "J.D. Salinger", 1951, "В наличии")
    # book2 = Book("War and Peace", "Leo Tolstoy", 1869, "В наличии")
    # with open("library.json", "a", encoding="cp1251") as file:
    #     json.dump(book2.__dict__, file, ensure_ascii=False, indent=4)
    while True:
        print(
            "Вас приветствует проект электронной библиотеки.\n"
            "1. Добавить книгу.\n" 
            "2. Вывести все книги.\n"
            "3. Найти книгу\n"
            "4. Удалить книгу.\n"
            "5. Изменить статус книги.\n"
            "6. Выход\n"
        )
        match input():
            case "1":
                title = input("Название: ")
                author = input("Автор: ")
                year = int(input("Год: "))
                status = "В наличии"
                book = Book(title, author, year, status)
                write_book(book)
            case "2":
                print_all_books()
            case "3":
                match input("1. По названию\n2. По автору\n3. По году\n"):
                    case "1":
                        title = input("Название: ")
                        with open("library.json", "r", encoding="cp1251") as file:
                            books = json.load(file)
                            filtred_books = filter(lambda x: x["title"] == title, books)
                    case "2":
                        author = input("Автор: ")
                        with open("library.json", "r", encoding="cp1251") as file:
                            books = json.load(file)
                            filtred_books = filter(lambda x: x["author"] == author, books)
                    case "3":
                        year = int(input("Год: "))
                        with open("library.json", "r", encoding="cp1251") as file:
                            books = json.load(file)
                            filtred_books = filter(lambda x: x["year"] == year, books)
            case "4":
                del_id = input("Введите номер книги: ")
                with open("library.json", "r", encoding="cp1251") as file:
                    books = json.load(file)
                    filtred_books = list(filter(lambda x: x["id"] == del_id, books))
                with open("library.json", "w", encoding="cp1251") as file:
                    json.dump(filtred_books, file, ensure_ascii=False, indent=4)
            case "5":
                book_id = input("Введите номер книги: ")
                new_status = input("Новый статус: ")
                change_book_status(book_id, new_status)
            case "6":
                exit()

