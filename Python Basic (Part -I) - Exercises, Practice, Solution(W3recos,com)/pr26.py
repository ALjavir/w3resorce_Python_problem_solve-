#pro26. Write a Python program to create a histogram from a given list of integers.
a = [1,2,3,2,1]
for i in a:
# 1st way
    if i == a[0]:
        print(a[0]*("*"))
    elif i == a[1]:
        print(a[1]*("*")) 
    elif i == a[2]:
        print(a[2]*("*"))
    elif i == a[3]:
        print(a[3]*("*")) 
#2nd way
    print(i*"*")