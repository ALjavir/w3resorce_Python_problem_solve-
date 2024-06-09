#pro37. Write a Python program to display your details like name, age, address in three different lines.
# a = input("Enter your name: ")
# b = input("Enetr your age: ")
# c = input("Enter your address: ")
# print(a)
# print(b)
# print(c)

class new:
    def __init__( self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

call = new("Tonmoy", "20", "aka")

#print(f"{self.name}\n{self.age}\n{self.address}") 
print(call)       