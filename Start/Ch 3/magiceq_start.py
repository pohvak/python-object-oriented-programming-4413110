# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: the __eq__ method checks for equality between two objects
    def __eq__(self, other):
        if not isinstance(other, Book):
            return ValueError("Cannot compare Book with non-Book object")
        return (self.title == other.title and
                self.author == other.author and
                self.price == other.price)

    # TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, other):
        if not isinstance(other, Book):
            return ValueError("Cannot compare Book with non-Book object")
        return self.price >= other.price

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, other):
        if not isinstance(other, Book):
            return ValueError("Cannot compare Book with non-Book object")
        return self.price < other.price


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality
print(b1 == b3)
print(b1 == b2)
print(b1 == 42)

# TODO: Check for greater and lesser value
print(b2 >= b1)
print(b2 < b1)


# TODO: Now we can sort them too
books = [b1, b2, b3, b4]
books.sort()
print([book.title for book in books])
