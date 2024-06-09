#pro 16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
def given(n):
    if n<= 17:
        return 17 - n
    else:
        return (n- 17)*2

print(given(14))
print(given(22))        
