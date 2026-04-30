'''class Student: 
    def __init__(self, fullname , marks ):
        self.fullname = fullname
        self.marks = marks
    
s1 = Student("Kavya Kushwaha" , 97)
print(s1.fullname , s1.marks)

s2 = Student("Shivam Maurya", 99)
print(s2.fullname, s2.marks)'''

class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
    
s1 = Student("Kavya Kushwaha", 97)
print(s1.name, s1.marks)