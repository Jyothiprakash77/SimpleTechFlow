# Q8. Create a HotelRoom class that:
# •	Keeps a base price per night (shared).
# •	Each room has room_number, nights_booked, and guest_name.
# •	Has a method to calculate total bill.
# •	Allows updating the base price across all rooms.
# •	Provides a static utility to check if a number of nights is valid (e.g., positive integer only).
# Demonstrate:
# 1.	Creating rooms and bookings.
# 2.	Changing base price.
# 3.	Checking bill updates and validation.
class HostelRoom:
    Base_price=600
    def __init__(self,room_number,nights_booked,guest_name):
        self.room_number=room_number
        self.nights_booked=nights_booked
        self.guest_name=guest_name
    def total_bill(self):
        return self.nights_booked*self.Base_price
    @classmethod
    def update_price(cls,new_price):
        cls.Base_price=new_price
    @staticmethod
    def valid_nights(n):
        if n!=int(n):
            print("Invalid")
            return False
        elif n<0:
            print("Invalid")
            return False
        else:
            return True
R101=HostelRoom(101,5,"Chiranjivi")
R102=HostelRoom(102,2,"Nagarjuna")
R907=HostelRoom(907,10,"Nicolus cage")
HostelRoom.update_price(700)
if R907.valid_nights(R907.nights_booked):
    print(R907.total_bill())
