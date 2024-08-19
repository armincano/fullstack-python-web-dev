from datetime import datetime

class LibraryResource:
    def __init__(self, title:str, author:str, publication_year :int):
        self._title = title
        self._author = author
        #try:
        current_year = datetime.now().year
        if publication_year > current_year:
            raise ValueError("El año de publicación no puede ser en el futuro.")
        self._publication_year = publication_year
        """except ValueError as e:
            print(f"Error initializing LibraryResource: {e}")
            self._publication_year = 0 # Set a default or fallback value"""

    @property
    def publication_year(self):
        return self._publication_year
    @publication_year.setter
    def publication_year(self, value):
        try:
            current_year = datetime.now().year
            if value > current_year:
                raise ValueError("El año de publicación no puede ser en el futuro.")
            self._publication_year = value
        except ValueError as e:
            print(f"Error updating publication_year: {e}")
        
    def info(self):
        return f"✎﹏﹏﹏﹏﹏﹏﹏﹏﹏\nTítulo: {self._title}\nAutor: {self._author}\nAño de publicación: {self._publication_year}\n﹏﹏﹏﹏﹏﹏﹏﹏﹏₊∘"
    
class Book(LibraryResource):
    def __init__(self, title:str, author:str, publication_year:int, total_pages:int):
        super().__init__(title, author, publication_year )
        self._total_pages = total_pages
        
    def info(self):
        return f"✎﹏﹏﹏﹏﹏﹏﹏﹏﹏\nTítulo: {self._title}\nAutor: {self._author}\nAño de publicación: {self._publication_year}\nNúmero de páginas: {self._total_pages}\n﹏﹏﹏﹏﹏﹏﹏﹏﹏₊∘"
    
class Magazine(LibraryResource):
    def __init__(self, title:str, author:str, publication_year:int, issue_number:int):
        super().__init__(title, author, publication_year)
        self._issue_number=issue_number
        
    def info(self):
        return f"✎﹏﹏﹏﹏﹏﹏﹏﹏﹏\nTítulo: {self._title}\nAutor: {self._author}\nAño de publicación: {self._publication_year}\nNúmero de edición: {self._issue_number}\n﹏﹏﹏﹏﹏﹏﹏﹏﹏₊∘"
    
class Newspaper(LibraryResource):
    def __init__(self, title:str, author:str, publication_year:int, publication_date:str):
        super().__init__(title, author, publication_year)
        self._publication_date = publication_date
        
    def info(self):
        return f"✎﹏﹏﹏﹏﹏﹏﹏﹏﹏\nTítulo: {self._title}\nAutor: {self._author}\nAño de publicación: {self._publication_year}\nFecha: {self._publication_date}\n﹏﹏﹏﹏﹏﹏﹏﹏﹏₊∘"