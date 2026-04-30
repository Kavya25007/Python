class Grandparent:
    def __init__(self, surname):
        self.surname = surname


class Parent(Grandparent):
    def __init__(self, surname, skin_tone):
        super().__init__(surname)
        self.skin_tone = skin_tone


class Child(Parent):
    def __init__(self, name, surname, skin_tone):
        super().__init__(surname, skin_tone)
        self.name = name


child1 = Child("Kavya", "Kushwaha", "Neutral")
print(child1.name, child1.surname)
print("Skin tone of child1 is",child1.skin_tone)
    
