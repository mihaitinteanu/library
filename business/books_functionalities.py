class BookController:
    """
    A class that manages all the book related functionalities.
    Intermediates communication between the UI and the repository.
    Attributes:
        book_repository: An object that stores the books
        book_validator: An object that validates the books
    """
    def __init__(self, book_repository, book_validator):
        self.book_repository = book_repository
        self.book_validator = book_validator

    def get_books(self):
        """
        Method that gets all the books available in the repository.
        :return: the method from the repo that gets all the books
        """
        return self.book_repository.get_books()

    def controller_add_book(self, book):
        """
        Method that validates the user input and calls the method
        that adds a book to the repository.
        :param book: a book object
        :return: None
        """
        self.book_validator.validate_book(book)
        self.book_repository.add_book(book)

    def controller_del_book(self, book_id):
        """
        Method that validates the user input and calls the method
        that deletes a book from the repository.
        :param book_id: a book id
        :return: None
        """
        if book_id <= 0:
            raise ValueError("Book id cannot be negative!")
        self.book_repository.delete_book(book_id)

    def controller_update_book(self, book):
        """
        Method that validates the user input and calls the method
        that updates a book from the repository.
        :param book: a book object
        :return: None
        """
        self.book_validator.validate_book(book)
        self.book_repository.update_book(book)