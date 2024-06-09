#6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
#If the given string already ends with 'ing' then add 'ly' instead.
#If the string length of the given string is less than 3, leave it unchanged
a = "gooo"
if len(a)<3:
    print(a)
elif len(a)>3 and a[-3:] == "ing":
    print(a+"ly")   
elif len(a)>3 and a[-3:] != "ing":
    print(a+"ing")     