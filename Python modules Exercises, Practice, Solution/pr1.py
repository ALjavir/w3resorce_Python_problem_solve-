#1. Write a Python program to generate a random color hex,
# a random alphabetical string,
# random value between two integers (inclusive) 
# and a random multiple of 7 between 0 and 70. Use random.randint()
import random
import string
# a = "#{:06x}".format(random.randint(0, 0xffffff))
# print("Random color hex:",a)

maxL = 15
for i in range(0,maxL):
    b = random.choice(string.ascii_letters)
    print("\nRandom alp: ",b)

c = random.randint(0, 7)
print(c*7)