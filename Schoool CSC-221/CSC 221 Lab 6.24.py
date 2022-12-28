dollar = 0
quarter = 0
dime = 0
nickel = 0
penny = 0

amount = int(input())

if(amount == 0):
    print("No change")

while(amount > 0):
    if(amount >= 100):
        amount -= 100
        dollar += 1
    elif(amount >= 25):
        amount -= 25
        quarter += 1
    elif(amount >= 10):
        amount -= 10
        dime += 1
    elif(amount >= 5):
        amount -= 5
        nickel += 1
    elif(amount >= 1):
        amount -= 1
        penny += 1

if(dollar > 0):
    if(dollar == 1):
        print(dollar, "Dollar")
    else:
        print(dollar, "Dollars")
if(quarter > 0):
    if(quarter == 1):
        print(quarter, "Quarter")
    else:
        print(quarter, "Quarters")
if(dime > 0):
    if(dime == 1):
        print(dime, "Dime")
    else:
        print(dime, "Dimes")
if(nickel > 0):
    if(nickel == 1):
        print(nickel, "Nickel")
    else:
        print(nickel, "Nickels")
if(penny > 0):
    if(penny == 1):
        print(penny, "Penny")
    else:
        print(penny, "Pennies")
