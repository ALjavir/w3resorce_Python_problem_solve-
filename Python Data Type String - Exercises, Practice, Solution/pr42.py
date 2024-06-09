#42. Write a Python program to count repeated characters in a string
s = 'thequickbrownfoxjumpsoverthelazydog'
b = {i: s.count(i) for i in s}
# for i in s:
#    b =  s.count(i)

#print(s)
print(b)