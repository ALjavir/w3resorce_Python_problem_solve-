#35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5
def fun(num1,num2):

    a = num1+num2
    if a == 5 or num1 == 5 or num2 == 5 or (num1 - num2) == 5:
        return True
    else:
        return False        

a = fun(int(input("Enter num1: ")), int(input("Enter num2: ")))
print(a)        