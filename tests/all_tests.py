from business.books_functionalities import BookController
from business.clients_functionalities import ClientController
from domain.books import Book
from domain.clients import Client
from repository.book_repository import BookRepository
from repository.client_repository import ClientRepository
from validate.validate_book import BookValidator
from validate.validate_client import ClientValidator


class TestBooks:
    def test_domain(self):
        book = Book(1, "Ion", "Roman", "Rebreanu")
        assert book.get_book_id() == 1
        assert book.get_title() == "Ion"
        assert book.get_description() == "Roman"
        assert book.get_author() == "Rebreanu"

    def test_validator(self):
        validator = BookValidator()
        valid_book = Book(1, "Ion", "Roman", "Rebreanu")
        invalid_book = Book(-1, "", "", "")

        try:
            validator.validate_book(valid_book)
        except ValueError:
            assert False

        try:
            validator.validate_book(invalid_book)
            assert False
        except ValueError:
            assert True

    def test_repository(self):
        book_repo = BookRepository()
        book = Book(1, "Ion", "Roman", "Rebreanu")

        # test get_books
        book_repo.add_book(book)
        books = book_repo.get_books()
        assert len(books) == 1
        assert books[0] == book

        # test add_book
        book_2 = Book(2, "Harap-Alb", "Basm", "Creanga")
        book_repo.add_book(book_2)
        my_books = book_repo.get_books()
        assert len(my_books) == 2
        assert my_books[0] == book
        assert my_books[1]== book_2

        # test raise: adding a duplicate
        duplicate_book = Book(1, "ceva", "ceva", "ceva")
        try:
            book_repo.add_book(duplicate_book)
            assert False
        except ValueError:
            pass

        # test delete_book
        book_repo.delete_book(1)
        books = book_repo.get_books()
        assert len(books) == 1
        assert books[0] == book_2

        # test raise: deleting a book that doesn't exist
        try:
            book_repo.delete_book(9)
            assert False
        except ValueError:
            pass

        # test update_book
        new_book = Book(2, "a", "b", "c")
        book_repo.update_book(new_book)
        books = book_repo.get_books()
        assert len(books) == 1
        assert books[0] == new_book

        # test raise: updating a book that doesn't exist
        book_not_in_repo = Book(9, 'a', 'a', 'a')
        try:
            book_repo.update_book(book_not_in_repo)
            assert False
        except ValueError:
            pass

    def test_controller(self):
        book_repo = BookRepository()
        book_validator = BookValidator()
        book_controller = BookController(book_repo, book_validator)
        book = Book(1, "Ion", "Roman", "Rebreanu")

        # test get_books
        book_controller.controller_add_book(book)
        books = book_controller.get_books()
        assert len(books) == 1
        assert books[0] == book

        # test controller_add_book
        book_2 = Book(2, "Harap-Alb", "Basm", "Creanga")
        book_controller.controller_add_book(book_2)
        books = book_controller.get_books()
        assert len(books) == 2
        assert books[0] == book
        assert books[1] == book_2

        # test raise: adding a book that already exists
        duplicate_book = Book(1, "ceva", "ceva", "ceva")
        try:
            book_controller.controller_add_book(duplicate_book)
            assert False
        except ValueError:
            pass

        # test controller_delete_book
        book_controller.controller_del_book(1)
        books = book_controller.get_books()
        assert len(books) == 1
        assert books[0] == book_2

        # test raise: the book id is negative / deleting a book that doesn't exist
        try:
            book_controller.controller_del_book(-1)
            assert False
        except ValueError:
            pass

        try:
            book_controller.controller_del_book(9)
            assert False
        except ValueError:
            pass

        # test controller_update_book
        new_book = Book(2, "Ion", "Roman", "Rebreanu")
        book_controller.controller_update_book(new_book)
        books = book_controller.get_books()
        assert len(books) == 1
        assert books[0] == new_book

        # test raise: updating a book that doesn't exist
        book_not_exist = Book(10, "Ion", "Roman", "Rebreanu")
        try:
            book_controller.controller_update_book(book_not_exist)
            assert False
        except ValueError:
            pass

    def run_all_tests(self):
        print("Running book tests...")
        self.test_domain()
        self.test_validator()
        self.test_repository()
        self.test_controller()
        print("All book tests passed!")

class TestClients:
    def test_domain(self):
        client = Client(1, 'Mihai', '1234567890123')
        assert client.get_client_id() == 1
        assert client.get_name() == 'Mihai'
        assert client.get_cnp() == '1234567890123'

    def test_validator(self):
        validator = ClientValidator()
        valid_client = Client(1, 'Mihai', '1234567890123')
        invalid_client = Client(-1, '', '123456789012')
        try:
            validator.validate_client(valid_client)
        except ValueError:
            assert False

        try:
            validator.validate_client(invalid_client)
            assert False
        except ValueError:
            pass

    def test_repository(self):
        client_repo = ClientRepository()
        client_1 = Client(1, 'Mihai', '1234567890123')
        client_2 = Client(2, 'Alex', '3210987654321')

        # test add_client
        client_repo.add_client(client_1)
        client_repo.add_client(client_2)
        clients = client_repo.get_clients()
        assert len(clients) == 2
        assert clients[0] == client_1
        assert clients[1] == client_2

        # test raise: client already exists
        duplicate_client = Client(1, 'Mihai', '1234567890123')
        try:
            client_repo.add_client(duplicate_client)
            assert False
        except ValueError:
            pass

        # test del_client
        client_repo.del_client(2)
        clients = client_repo.get_clients()
        assert len(clients) == 1
        assert clients[0] == client_1

        # test raise: deleting a client that doesn't exist
        try:
            client_repo.del_client(9)
            assert False
        except ValueError:
            pass

        # test update_client
        new_client = Client(1, 'ceva', '1234567890123')
        client_repo.update_client(new_client)
        clients = client_repo.get_clients()
        assert len(clients) == 1
        assert clients[0] == new_client

        # test raise: updating a client that doesn't exist
        client_not_exist = Client(9, 'Mihai', '1234567890123')
        try:
            client_repo.update_client(client_not_exist)
            assert False
        except ValueError:
            pass

    def test_controller(self):
        client_repo = ClientRepository()
        client_validator = ClientValidator()
        client_controller = ClientController(client_repo, client_validator)
        client_1 = Client(1, 'Mihai', '1234567890123')
        client_2 = Client(2, 'Alex', '3210987654321')

        # test controller_add_client
        client_controller.controller_add_client(client_1)
        client_controller.controller_add_client(client_2)
        clients = client_controller.get_clients()
        assert len(clients) == 2
        assert clients[0] == client_1
        assert clients[1] == client_2

        # test raise: adding a client that already exists
        duplicate_client = Client(1, 'Mihai', '1234567890123')
        try:
            client_controller.controller_add_client(duplicate_client)
            assert False
        except ValueError:
            pass

        # test controller_del_client
        client_controller.controller_del_client(2)
        clients = client_controller.get_clients()
        assert len(clients) == 1
        assert clients[0] == client_1

        # test raise: deleting a client that doesn't exist / negative id
        try:
            client_controller.controller_del_client(-1)
            assert False
        except ValueError:
            pass

        try:
            client_controller.controller_del_client(100)
            assert False
        except ValueError:
            pass

        # test controller_update_client
        new_client = Client(1, 'abc', '1234567890123')
        client_controller.controller_update_client(new_client)
        clients = client_controller.get_clients()
        assert len(clients) == 1
        assert clients[0] == new_client

        # test raise: updating a client that doesn't exist
        client_not_exist = Client(100, 'Mihai', '1234567890123')
        try:
            client_controller.controller_update_client(client_not_exist)
            assert False
        except ValueError:
            pass

    def run_all_tests(self):
        print("Running client tests...")
        self.test_domain()
        self.test_validator()
        self.test_repository()
        self.test_controller()
        print("Client tests passed!")

class RunTests:
    def __init__(self):
        self.test_books = TestBooks()
        self.test_clients = TestClients()

    def run_all_tests(self):
        print("Running tests...")
        self.test_books.run_all_tests()
        self.test_clients.run_all_tests()
        print("Tests passed!")