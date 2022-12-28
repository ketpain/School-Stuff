keepRunning = True

while(keepRunning == True):
    text = str(input())
    if(text == 'done' or text == 'd' or text == 'Done'):
        keepRunning = False
    elif(keepRunning == True):
        print(text[::-1])
