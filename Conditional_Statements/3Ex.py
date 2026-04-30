a = input("Enter the comment to check whether it is spam comment or real comment")
a = a.lower()
if "make a lot of money" in a or "buy now" in a or "subscribe this" in a or "click this" in a:
    print("This comment is Spam")
else:
    print("This comment is real")