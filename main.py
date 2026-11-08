from UI.console import Console
from business.books_functionalities import BookController
from repository.book_repository import BookRepository
from validate.validate_book import BookValidator
from business.clients_functionalities import ClientController
from repository.client_repository import ClientRepository
from validate.validate_client import ClientValidator


def run():
    """
    Runs the application.
    :return: None
    """
    book_repository = BookRepository()
    book_validator = BookValidator()
    book_controller = BookController(book_repository, book_validator)

    client_repository = ClientRepository()
    client_validator = ClientValidator()
    client_controller = ClientController(client_repository, client_validator)

    console = Console(book_controller, client_controller)

    while True:
        command_text = input("Write a command: ").strip().lower()
        if command_text == '':
            continue
        if command_text == 'exit':
            print("Bye!")
            return
        command_parts = command_text.split()
        command_name = command_parts[0]
        parameters = command_parts[1:]
        if command_name in console.commands:
            console.commands[command_name](parameters)
        else:
            print("Unknown command.")

run()