# Q9. Design a LibraryMember class that:
# •	Tracks total active members.
# •	Each member has a name and books_borrowed count.
# •	Has a function to borrow books, with borrowing limit common to all.
# •	Allows updating borrowing limit globally.
# •	Has a static function to check if book title is valid (non-empty string, reasonable length).
# Demonstrate:
# 1.	Borrowing books for multiple users.
# 2.	Changing borrowing limits.
# 3.	Validating book titles before borrowing.
class LibraryMember:
    Members=[]
    limit=5
    def __init__(self,name):
        self.name=name
        self.book_borrowed=0
    def Borrow_book(self,title):
        if self.book_borrowed<LibraryMember.limit or self.valid_title(title):
            print("Can't able give book")
            return False
        else:
            self.book_borrowed += 1
            return True
    @staticmethod
    def invalid_title(title):
        if title == "" or len(title)>10:
            return True
        return False
Henry=LibraryMember("Henry")
Ramesh=LibraryMember("Ramesh")
LibraryMember.limit=10
Henry.Borrow_book("")

