#pro36. Write a Python program to add two objects if both objects are an integer type.
def fun(a,b):
    if type(a) ==int and type(b) == int:
        return a+b
    else:
        return("Plese enter both integer")

print(fun(50, 3))           