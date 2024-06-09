#pro113. Write a Python program to input a number, if it is not a number generates an error message
while True:
    try:
        a = int(input("Enter a number: "))
        #break
    except ValueError:
        print("Please enter a valied number and try agin.....:)")
        print()