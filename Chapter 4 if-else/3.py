time = int(input("Enter the time"))
print("The time is", time)
if(time< 12 ) and (time>0):
    print("Good Morning")
elif(time>= 12) and (time < 17 ):
    print("Good Afternoon")
elif(time>= 17 ) and (time< 21 ):
    print("Good Evening")
elif(time<=23):
    print("Good Night") 
else:
    print("Invalid Time")