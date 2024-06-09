#pro1. Write a Python function that takes a sequence of numbers 
# And determines whether all the numbers are different from each other.
def check_number(n):
    if len(n) == len(set(n)):
        return True
    else:
        return False

print(check_number([1,3,4,5,67,6]))            