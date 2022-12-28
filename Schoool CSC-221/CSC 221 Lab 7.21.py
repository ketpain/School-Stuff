#i becomes 1
#a becomes @
#m becomes M
#B becomes 8
#s becomes $

word = str(input())

password = word.replace("i", "1")
password = password.replace("a", "@")
password = password.replace("m", "M")
password = password.replace("B", "8")
password = password.replace("s", "$")
password = password + "!"

print(password)