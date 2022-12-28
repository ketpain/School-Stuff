x = int(input())
dislist = []


i = 1
while i <= x:
    y = float(input())
    dislist.append(y)
    i += 1

q = max(dislist)


for item in dislist:
    item = item / q
    print('{:.2f}'.format(item))