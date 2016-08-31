class Book:
    """Informtion about a book, including title, list of authors, publisher,
    ISBN, and price.
    """

    def __init__(self, title, authors, publisher, isbn, price):
        """(Book, str, list of str, str, str, str, number) -> NoneType

        Create a new book entitled title, written by the people in authors,
        published by the publisher, with ISBN isbn and costing price dollars.

        >>>python_book = Book( \
                'Practical Programming', \
                ['Campbell', 'Gries', 'Montojo'], \
                'Pragmatic Bookshelf', \
                '978-1-93778-545-1', \
                25.0)
        >>>python_book.title
        'Practical Programming'
        >>>python_book.authors
        ['Campbell', 'Gries', 'Montojo']
        >>>python_book.publisher
        'Pragmatic Bookshelf'
        >>>python_book.ISBN
        '978-1-93778-545-1'
        >>>python_book.price
        25.0
        """
        self.title = title
        # Copy the authors list in case the caller modifies the list later.
        self.authors = authors[:]
        self.publisher = publisher
        self.ISBN = isbn
        self.price = price

    def __eq__(self, other):
        """(Book, Book) -> bool
        Return True iff this book and other have the same ISBN.
        """
        return self.ISBN == other.ISBN

    def num_authors(self):
        """(Book) -> int

        Return the number of authors of this book.
        """
        return len(self.authors)

    def __str__(self):
        """(Book) -> str
        Return a human-readable string representation of this Book.
        """
        return """Title: {0}
Authors: {1}
Publisher: {2}
ISBN: {3}
Price: ${4}""".format(self.title, ', '.join(self.authors), self.publisher,
                      self.ISBN, self.price)
