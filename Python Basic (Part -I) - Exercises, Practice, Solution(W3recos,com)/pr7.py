#pr7. Write a Python program to accept a filename from the user and print the extension of that
file_name = input("Enter the file name: ")
a = file_name.split(".")
print(repr(a[-1]))