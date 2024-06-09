#12. Write a Python program to count the occurrences of each word in a given sentence.
a = "go to hell go go go"
b = a.split()
c = {i:b.count(i) for i in b}
print(c)
