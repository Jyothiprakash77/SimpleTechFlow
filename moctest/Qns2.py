class Book:
    total_books=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        Book.total_books+=1
    @classmethod
    def from_string(cls,book_str):
        title,author=book_str.split("-")
        return cls(title,author)
B1=Book("Game of thrones","Hubble thomson")
B2=Book.from_string("Harry porther-Sean ukasa")
print(B1.title,B1.author)
print(B2.title,B2.author)
print(Book.total_books)