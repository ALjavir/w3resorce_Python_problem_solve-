#pro68. Write a Python program to calculate the sum of the digits in an integer.
a = input("Enter a number: ")
num = 0
for i in str(a):
    num += int(i)
print(num)    