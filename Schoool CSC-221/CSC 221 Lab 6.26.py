par = 0
par = int(input())
isValid = True

if(par < 3 or par > 5):
    print("Error")
    isValid = False

stroke = int(input())

if(stroke == par - 2 and isValid == True):
    print("Eagle")
if(stroke == par - 1 and isValid == True):
    print("Birdie")
if(stroke == par and isValid == True):
    print("Par")
if(stroke == par + 1 and isValid == True):
    print("Bogey")