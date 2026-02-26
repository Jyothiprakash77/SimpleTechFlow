class Building:
    no_ofRooms=10
    no_ofBuildings=0
    def __init__(self,name):
        self.Building_name=name
        self.wifi=False
        Building.no_ofBuildings+=1
    def change_rooms(self,nor):
        Building.no_ofRooms=nor

Orange_rooms=Building("OrangeRooms")
CV_stays=Building("CV Stays")
print(Building.no_ofBuildings)