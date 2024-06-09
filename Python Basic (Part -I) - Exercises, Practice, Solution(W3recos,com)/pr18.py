#pro18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum
def sumn(x, y, z):

    sum = x + y + z
    
    if x == y == z:
        sum = sum *3
    return sum
     
print(sumn(1, 2, 3))
print(sumn(4, 4, 4))    