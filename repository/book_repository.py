class BookRepository:
    """
    A class to store all the book related operations (CRUD).
    Attributes:
        books: a dictionary with all the books registered in the repository;
        the key is the book id and the value is the book object;
    """
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        """
        Adds a book to the repository.
        :param book: a Book object to be added
        :return: None
        """
        book_id = book.get_book_id()
        if book_id in self.books.keys():
            raise ValueError("The book already exists!")
        self.books[book_id] = book

    def get_books(self):
        """
        Method to get all books
        :return: list with the values of the books
        """
        return list(self.books.values())

    def delete_book(self, book_id):
        """
        Method to delete a book from the repository.
        :param book_id: a Book object to be deleted
        :return: None
        """
        if book_id in self.books.keys():
            del self.books[book_id]
        else:
            raise ValueError("The book does not exist!")

    def update_book(self, updated_book):
        """
        Method to update a book from the repository.
        :param updated_book: a Book object to be updated
        :return: None
        """
        updated_book_id = updated_book.get_book_id()
        if updated_book_id in self.books.keys():
            self.books[updated_book_id] = updated_book
        else:
            raise ValueError("The book does not exist!")