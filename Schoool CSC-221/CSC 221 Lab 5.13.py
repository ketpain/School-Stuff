phone_number = int(input())

lastFour = phone_number % 10000

firstThree = phone_number // 10000000

middleThree = phone_number // 10000 % 1000

print(f'({firstThree}) {middleThree}-{lastFour}')
