#31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

#1st way
#  def GCD(x,y):
#     z = x%y
#     while z:
#         x = y
#         y = z
#         z = x%y
#     return y
# print(GCD(12, 17))        

#2nd way
# import math

# x = 12
# y = 17
# gcd1 = math.gcd(x, y)
# print(gcd1)