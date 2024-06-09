#pro25. Write a Python program to check whether a specified value is contained in a group of values. 
'''Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''
def group_value(num):
    a = int(input("Enter the value you wanto chcek: "))
    if a in num:
        return True
    else:
        return False
n = group_value([1,2,3,4,5,6,7,8,9]) 
print("Test Data")
print(n)           
