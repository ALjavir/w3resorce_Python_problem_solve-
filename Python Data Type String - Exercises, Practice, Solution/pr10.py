#10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
a = "1,2,3,4,5"
a1 = a
b = a.replace(a[:1], a[-1:])
c = b.replace(b[-1:], a1[:1])
print(a[:1])
print(b)
print(c)
x = a[-1:] + a[1:-1] + a[:1]
print(x)