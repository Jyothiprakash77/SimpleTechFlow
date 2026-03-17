# Q6. Create a class Book with:
# •	instance attributes title, author
# •	a class variable total_books
# •	a class method from_string(cls, book_str) that creates an object from "title-author" format
# •	a static method is_valid_title(title) that checks if title has at least 3 characters
# •	increment total_books for every book created
# Demonstrate:
# •	Creating books using both the constructor and the class method
# •	Validating titles before creation
class book:
    total_books=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        book.total_books+=1
    @classmethod
    def from_string(cls,book_str):
        title,author=book_str.split("-")
        return cls(title,author)
    @staticmethod
    def is_valid_title(title):
        return len(title)>3
B1=book("naa savunenu sasta","prakash")
print(B1.title)
B2=book.from_string("Magic-Ray")
print(B2.title)
print(B2.is_valid_title(B2.title))

