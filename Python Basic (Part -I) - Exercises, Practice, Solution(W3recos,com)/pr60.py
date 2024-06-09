#pro60. Write a Python program to calculate the hypotenuse of a right angled triangle.
from math import sqrt
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = sqrt(a**2 + b**2)
print("hypotenuse",c)