red = int(input())
green = int(input())
blue = int(input())

#red = red - green
#blue = blue - green
#green = green - green

#print(red, green, blue)

smallestValue = False

if(red < green and red < blue):
    green = green - red
    blue = blue - red
if(blue < green and blue < red):
    green = green - blue
    red = red - blue
if(green < red and green < blue):
    blue = blue - green
    red = red - green
print(red, green, blue)