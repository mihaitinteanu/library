class BookValidator:
    """
    A class that helps with the validation of books.
    """
    def validate_book(self, book):
        errors = []

        if book.get_book_id() <= 0:
            errors.append('Book id cannot be negative!')

        if not str(book.get_title()).strip():
            errors.append('Book title cannot be empty!')

        if not str(book.get_description()).strip():
            errors.append('Book description cannot be empty!')

        if not str(book.get_author()).strip():
            errors.append('Book author cannot be empty!')

        if len(errors) > 0:
            raise ValueError("\n".join(errors))