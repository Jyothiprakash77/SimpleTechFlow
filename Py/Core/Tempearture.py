# Q5. Create a class Temperature with:
# •	instance attribute celsius
# •	a static method to_fahrenheit(celsius)
# •	an instance method show_conversion() that uses the static method to print both values.
class Temperature:
    def __init__(self,temp):
        self.celsius=temp
    def show_conversion(self):
        self.Fahrenheit=0
        self.Fahrenheit=self.to_fahrenheit(self.celsius)
        print(f"Temperature in Celsius->{self.celsius}")
        print(f"Temperature in Fahrenheits->{self.Fahrenheit}")
    def show_Fahrenheit(self):
        print(self.Fahrenheit)
    @staticmethod
    def to_fahrenheit(C):
        return C*1.8+32
T1=Temperature(90)
T1.show_conversion()
T1.show_Fahrenheit()
