#3. Write a Python program to check if a given function is a generator or not.
# Use types.GeneratorType()
import types
def a(x):
    yield x
        
def b(y):
    yield y

def add(x, a):
    yield x + y

print(isinstance(a(456), types.GeneratorType))
print(isinstance(b(823), types.GeneratorType))
print(isinstance(add(a,b), types.GeneratorType))