with open("practice.txt","r")as f:

    data = f.read()
    newdata =  data.replace("Python", "Java")
    print(newdata)