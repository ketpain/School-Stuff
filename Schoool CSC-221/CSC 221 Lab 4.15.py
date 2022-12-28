import math

keyFrequency = float(input())

nextFrequency1 = keyFrequency * math.pow(math.pow(2,0.0833333),1)
nextFrequency2 = keyFrequency * math.pow(math.pow(2,0.0833333),2)
nextFrequency3 = keyFrequency * math.pow(math.pow(2,0.0833333),3)
nextFrequency4 = keyFrequency * math.pow(math.pow(2,0.0833333),4)

print(f'{keyFrequency:.2f} {nextFrequency1:.2f} {nextFrequency2:.2f} {nextFrequency3:.2f} {nextFrequency4:.2f}')
