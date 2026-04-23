class LibraryBook:
    Borrow_Count=0
    Max_Borrow=10
    def __init__(self,name,ISBN):
        if LibraryBook.Valid_ISBN(ISBN):
            print("Invalid ISBN")
            return None
        self.name=name
        self.ISBN=ISBN
        self.Borrow=False
    def BorrowBook(self):
        if LibraryBook.Borrow_Count>LibraryBook.Max_Borrow or self.Borrow==True:
            print("Can't able to Borrow")
            return None
        self.Borrow=True
        LibraryBook.Borrow_Count+=1
    def ReturnBook(self,name):
        self.Borrow=False
        LibraryBook.Borrow_Count-=1
    @classmethod
    def change_MaxBorrow(cls,newMax):
        cls.Max_Borrow=newMax
    @staticmethod
    def Valid_ISBN(ISBN):
        if len(str(ISBN))>13 or len(str(ISBN))<13:
            return True
        elif int(ISBN)!=ISBN:
            return True
        return False
TOE=LibraryBook("Theory of everything",6756789890887)
TOE.BorrowBook()
print(TOE.Borrow)
print(TOE.Borrow_Count)

