#pro27. Write a Python program to concatenate all elements in a list into a string and return it.

a = ["Tonmoy","1","2",3,4,5]
for i in a:
    b = "".join(str(i))
    print(b,end="") 