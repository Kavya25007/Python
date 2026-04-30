class Student:
    school = "ABC School"   # ✅ class attribute (added)

    def __init__(self, name, marks):
        self.name = name     # instance attribute
        self.marks = marks   # instance attribute

    def get_avg(self):
        total = 0
        for val in self.marks:
            total += val
        print("Hi", self.name, "from", Student.school)
        print("Your avg score is:", total / len(self.marks))


# object
s1 = Student("Tony Stark", [99, 98, 97])
s1.get_avg()