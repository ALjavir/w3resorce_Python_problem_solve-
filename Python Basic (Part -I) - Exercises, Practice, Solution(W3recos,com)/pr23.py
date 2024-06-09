#pro23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2
a = input("Enter the string: ")
b = int(input("How many copeis you want: "))
if len(a) <= 2:
    print(a * abs(b))
else:
    c = (a[0:2])
    print(c* abs(b))        
