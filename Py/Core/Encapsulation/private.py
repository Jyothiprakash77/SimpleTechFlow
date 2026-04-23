# Explain the difference.
# 10. Create a class using @property and @setter for a private attribute.
# Then:
# 1. Show correct usage
# 2. Show how forgetting to use underscore prefix breaks encapsulation
# 3. Show what happens if you implement a setter without validation
# Focus: Python-specific encapsulation pitfalls, misuse of properties.
class instagram:
    def __init__(self,username,password):
        self._username=username
        self.__password=password
    @property
    def password(self):
        return self.__password
    