# 3. Create a SecureFile class that:
# • stores content privately
# • provides a method read(password)
# • refuses access if the password is incorrect
# • logs an "Unauthorized attempt" internally (cannot be accessed from outside)
class SecureFile:
    def __init__(self,password):
        self.__password=password
        self.__File=[]
        self.__Photos=[]
    def setpassword(self,oldpassword,newpassword):
        if self.__password==oldpassword:
            self.__password=newpassword
        else:
            print("Invalid Attemp")
    def getFile(self,password):
        if self.__password==password:
            return self.__File
        else:
            print("Unauthorized attemp")
    def setFile(self,password,*file):
        if self.__password == password:
            self.__File.extend(list(file))
        else:
            print("Unauthorized attemp")
    def getPhotos(self,password):
        if self.__password==password:
            return self.__Photos
    def storePhotos(self,password,*photos):
        if self.__password==password:
            self.__Photos.extend(list(photos))
        else:
            print("Unauthorized attemp")
S1=SecureFile(9076)
S1.storePhotos(9076,"fire","human","Bike")
print(S1.getPhotos(9076))
S1.setFile(9070,"Iruvi","Ayra")
print(S1.getFile(9076))


