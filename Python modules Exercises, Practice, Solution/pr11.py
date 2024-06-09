#2. Write a Python program to check if a given value is a method of a user-defined class.
# Use types.MethodType()
import types
class Tonmoy():
    def x():
        return 1
    def y():
        return 1
def b():
        return 1

print(isinstance(Tonmoy().x, types.MethodType))
print(isinstance(Tonmoy().y, types.MethodType))
print(isinstance(max, types.MethodType))
print(isinstance(abs, types.MethodType))      
print(isinstance(b, types.MethodType))          