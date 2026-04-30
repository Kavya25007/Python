class Grandparent:
    def __init__(self, surname, address):
        self.surname = surname
        self.address = address
   
class Parent(Grandparent):
    def __init__(self, surname, address, skintone, height):
        super().__init__(surname, address)
        self.skintone = skintone
        self.height = height

class Child(Parent):
    def __init__(self, name, surname, address, skintone, height):
        super().__init__(surname, address, skintone, height)
        self.name = name
   
c1 = Child("Kavya", "Black", "Unnao, Uttarpradesh", "Neutral", 5.2)
print(c1.name , c1.surname)
print("Address of child = ",c1.address)
print("The skintone of child is ",c1.skintone)