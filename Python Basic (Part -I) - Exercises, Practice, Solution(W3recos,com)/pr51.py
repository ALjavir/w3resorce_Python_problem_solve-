#pro51.Write a Python program to determine profiling of Python programs.
import cProfile
def summ(x,y,z):
    if x == y or y == z or z == x:
        print("0")
    else:
        return (x+y+z)

print(summ(1, 2, 3))      
cProfile.run("summ()")