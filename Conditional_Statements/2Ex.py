a = int(input("Enter the marks of Subject 1= "))
b = int(input("Enter the marks of Subject 2= "))
c = int(input("Enter the marks of Subject 3= "))
total = (a+b+c)/3
if (a >= 33) and (b >= 33) and (c >= 33) and ( total >= 40):
    print("Congratulations , You  have passed the exam")
else:
    print("Sorry , You have failed the exam")
