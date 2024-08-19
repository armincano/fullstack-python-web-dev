class Book:
    def __init__(self, author: str, title: str, publication_year: int = None):
        self._author = author
        self._title = title
        self._publication_year = publication_year
        
    def __dict__(self):
        book_dict = {
            'author': self._author,
            'title': self._title
        }
        if self._publication_year is not None:
            book_dict['publication_year'] = self._publication_year
        return book_dict

book_1 = Book('Dan Brown', 'The Da Vinci Code', 2003)
print(book_1.__dict__())

book_2 = Book('Dan Brown', 'Inferno')
print(book_2.__dict__())