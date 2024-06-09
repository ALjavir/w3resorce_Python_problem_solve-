#pro20. Write a Python program to get a string which is n (non-negative integer) copies of a given string
a = input(" Enter the string: ")
b = int(input("Enter the number of coptes: "))
c = a * abs(b)
print(c)