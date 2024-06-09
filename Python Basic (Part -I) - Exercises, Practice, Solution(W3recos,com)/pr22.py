#pro22. Write a Python program to count the number 4 in a given list.
def count_4(nums):
    count = 0
    for i in nums:
        if i == 4:
            count = count + 1
    return count        
a = count_4([1,2,3,44,4,4,4,4,4,5,6,7,8])            
print(a)