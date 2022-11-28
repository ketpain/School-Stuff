integer1 = int(input())
integer2 = int(input())
isValid = True

if(integer2 < integer1):
    print("Second integer can't be less than the first.", end= '')
    isValid = False

if(isValid == True):
    while(integer1 <= integer2):
        print(integer1, end= ' ')
        integer1 += 5
print()