class Library:
    noof_library=0
    def __init__(self,name,noof_books):
        self.library_name=name
        self.Noof_books=noof_books
        Library.noof_library+=1
L1=Library("CVLibrary",10)
print(L1.noof_library)
L2=Library("GovtLibrary",20)
L2.noof_library=5
print(L2.noof_library)
#A)1
#  1
#B)2
#  2
#C)1
#  5
#D)5
#  1