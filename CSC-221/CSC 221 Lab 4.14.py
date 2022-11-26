import math

x = float(input())
y = float(input())
z = float(input())

#Given three floating-point numbers x, y, and z, output x to the power of z, x to the power of (y to the power of z), the absolute value of (x minus y), and the square root of (x to the power of z).

#Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
#print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f} {your_value4:.2f}')

print(f'{math.pow(x,z):.2f} {math.pow(x,math.pow(y,z)):.2f} {math.fabs(x - y):.2f} {math.sqrt(math.pow(x,z)):.2f}')