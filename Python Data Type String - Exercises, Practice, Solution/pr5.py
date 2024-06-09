#5. Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.

a = "abc"
b = "xyz"
c = b[:2] + a[:1], b[1:]+a[2:]
print(c)