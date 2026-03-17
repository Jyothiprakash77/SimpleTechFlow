class Building:
    no_ofRooms=10
    no_ofBuildings=0
    def __init__(self,name):
        self.Building_name=name
        self.wifi=False
        Building.no_ofBuildings+=1
    def change_rooms(self,nor):
        Building.no_ofRooms=nor
        print(f"Rooms changed to {Building.no_ofRooms}")

Orange_rooms=Building("OrangeRooms")
CV_stays=Building("CV Stays")
print(Building.no_ofBuildings)
CV_stays.change_rooms(6)