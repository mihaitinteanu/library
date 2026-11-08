from domain.books import Book
from domain.clients import Client

class Console:
    """
    A class that represents the console and handles the users commands (input)
    and printing messages (output) to the user.
    Attributes:
        book_controller: a class that represents the book controller and its
        methods related to the business logic.
        client_controller: a class that represents the client controller and
        its methods related to the business logic.
        commands: a dictionary with all the valid commands the app has.
    """
    def __init__(self, book_controller, client_controller):
        self.book_controller = book_controller
        self.client_controller = client_controller
        self.commands = {
            "books": self.print_books,
            "add_book": self.ui_add_book,
            "del_book": self.ui_del_book,
            "update_book": self.ui_update_book,
            "clients": self.print_clients,
            "add_client": self.ui_add_client,
            "del_client": self.ui_del_client,
            "update_client": self.ui_update_client
        }

    def print_books(self, parameters):
        """
        Method that prints all the books available to the user.
        :param parameters: empty list
        :return: None
        """
        try:
            if len(parameters) != 0:
                raise ValueError("Invalid number of parameters.")
            for book in self.book_controller.get_books():
                print("Book id: {} Book title: {} Book description: {} Book author: {}".format(book.get_book_id(), book.get_title(), book.get_description(), book.get_author()))
        except ValueError as er:
            print(er)

    def ui_add_book(self, parameters):
        """
        Method that creates the object book and passes it to the
        controller method.
        :param parameters: a list with the attributes of a new book
        :return: None
        """
        try:
            if len(parameters) != 4:
                raise ValueError("Invalid number of parameters.")
            try:
                book_id = int(parameters[0])
            except ValueError:
                raise ValueError("Invalid book id! Must be an integer!")

            book = Book(book_id, parameters[1], parameters[2], parameters[3])
            self.book_controller.controller_add_book(book)
            print("Book added successfully!")
        except ValueError as er:
            print(er)

    def ui_del_book(self, parameters):
        """
        Method that takes the id of a book to be deleted and passes it to the
        controller method.
        :param parameters: a list with a book id
        :return: None
        """
        try:
            if len(parameters) != 1:
                raise ValueError("Invalid number of parameters.")
            try:
                book_id = int(parameters[0])
            except ValueError:
                raise ValueError("Invalid book id! Must be an integer!")

            self.book_controller.controller_del_book(book_id)
            print("Book deleted successfully!")
        except ValueError as er:
            print(er)

    def ui_update_book(self, parameters):
        """
        Method that creates a book object from the attributes given
        by the users and passes it to the controller method.
        :param parameters: a list with the attributes of a new book
        :return: None
        """
        try:
            if len(parameters) != 4:
                raise ValueError("Invalid number of parameters.")
            try:
                book_id = int(parameters[0])
            except ValueError:
                raise ValueError("Invalid book id! Must be an integer!")

            book = Book(book_id, parameters[1], parameters[2], parameters[3])
            self.book_controller.controller_update_book(book)
            print("Book updated successfully!")
        except ValueError as er:
            print(er)

    def print_clients(self, parameters):
        """
        Method that prints all the clients available to the user.
        :param parameters: empty list
        :return: None
        """
        try:
            if len(parameters) != 0:
                raise ValueError("Invalid number of parameters.")
            for client in self.client_controller.get_clients():
                print("Client id: {} Client name: {} CNP: {}".format(client.get_client_id(), client.get_name(), client.get_cnp()))
        except ValueError as er:
            print(er)

    def ui_add_client(self, parameters):
        """
        Method that creates the object client from the attributes given
        by the user and passes it to the controller method.
        :param parameters: a list with the attributes of a new client
        :return: None
        """
        try:
            if len(parameters) != 3:
                raise ValueError("Invalid number of parameters.")
            try:
                client_id = int(parameters[0])
                client_cnp = parameters[2]
            except ValueError:
                raise ValueError("Invalid client id! Must be an integer!")

            client = Client(client_id, parameters[1], client_cnp)
            self.client_controller.controller_add_client(client)
            print("Client added successfully!")
        except ValueError as er:
            print(er)

    def ui_del_client(self, parameters):
        """
        Method that takes the id of a client to be deleted and passes it to the
        controller method.
        :param parameters: a list with a client id
        :return: None
        """
        try:
            if len(parameters) != 1:
                raise ValueError("Invalid number of parameters.")
            try:
                client_id = int(parameters[0])
            except ValueError:
                raise ValueError("Invalid client id! Must be an integer!")

            self.client_controller.controller_del_client(client_id)
            print("Client deleted successfully!")
        except ValueError as er:
            print(er)

    def ui_update_client(self, parameters):
        """
        Method that creates a client object from the attributes given by
        the user and passes it to the controller method.
        :param parameters: a list with the attributes of a new client
        :return: None
        """
        try:
            if len(parameters) != 3:
                raise ValueError("Invalid number of parameters.")
            try:
                client_id = int(parameters[0])
                client_cnp = parameters[2]
            except ValueError:
                raise ValueError("Invalid client id! Must be an integer!")

            updated_client = Client(client_id, parameters[1], client_cnp)
            self.client_controller.controller_update_client(updated_client)
            print("Client updated successfully!")
        except ValueError as er:
            print(er)
