#20. Write a Python function to reverses a string if it's length is a multiple of 4
def fun(a):
    if len(a) <= 4 :
        return "".join(reversed(a))
    else:
        return a
x = fun("Ruby")
y = fun("Tonmoy")           
print(x)
print(y)