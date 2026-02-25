class Instagram:
    name="INSTAGRAM"
    No_Of_Users=0
    def __init__(self,name,Phn_no):
        self.username=name
        self.Phn_no=Phn_no
        self.follows=0
        Instagram.No_Of_Users+=1
    def change_name(self,new_name):
        self.username=new_name
        print(f"Username has been changed to {self.username}")
obj=Instagram("itz_flash",8967095409)
print(obj.username)
obj.change_name("flash_man")

