#pro33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
def summ(x,y,z):
    if x == y or y == z or z == x:
        print("0")
    else:
        return (x+y+z)

print(summ(2, 2, 3))        
