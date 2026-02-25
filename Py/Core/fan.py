class fan:
    name="wissuri"
    def __init__(self):
        self.name="strom"
        self.cost = 5699
        self.status=False
    def On_Click(self,NF):
        if NF.lower() == "on":
            self.turn_On()
        else:
            self.turn_Off()
    def turn_On(self):
        if self.status==False:
            print("fan is turn On")
            self.status = True
        else:
            print("fan is already on")
    def turn_Off(self):
        if self.status==True:
            print("fan is turn Off")
            self.status = False
        else:
            print("fan is already off")
    def fan_status(self):
        if self.status:
            print("power is on")
        else:
            print("power is off")
strom1=fan()
strom1.On_Click("On")
strom1.fan_status()