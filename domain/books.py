class Book:
    """
    A class to represent a book that has an id 'book_id',
    the title 'title', the description 'description' and the
    author 'author'. The class contains getters for each of
    the attributes 'book_id', 'title', 'description' and
    'author'.
    Attributes:
        book_id: The id of the book
        title: The title of the book
        description: The description of the book
        author: The author of the book
    """
    def __init__(self, book_id, title, description, author):
        self.book_id = book_id
        self.title = title
        self.description = description
        self.author = author

    def get_book_id(self):
        return self.book_id

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_author(self):
        return self.author
