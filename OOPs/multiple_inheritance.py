"""class Father():
    def __init__(self, surname, haircolour):
        self.surname = surname
        self.haircolour = haircolour

class Mother():
    def __init__(self, eyecolour, skintone):
        self.eyecolour = eyecolour
        self.skintone = skintone

class Child(Father, Mother):
    def __init__(self, name, surname, haircolour, eyecolour, skintone):
        # Calling both parent constructors
        Father.__init__(self, surname, haircolour)
        Mother.__init__(self, eyecolour, skintone)
        
        self.name = name

# Creating object
c1 = Child("Anvi", "Maurya", "Black", "Black", "Neutral")

# Output
print(c1.name, c1.surname)
print("Haircolour of child is", c1.haircolour)
print("Skintone of child is", c1.skintone)
print("Eyecolour of child is", c1.eyecolour)"""







import math

class Vector3D:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def add(self, v2):
        return Vector3D(self.x+v2.x, self.y+v2.y, self.z+v2.z)

    def cross(self, v2):
        x = self.y*v2.z - self.z*v2.y
        y = self.z*v2.x - self.x*v2.z
        z = self.x*v2.y - self.y*v2.x
        return Vector3D(x,y,z)