#pro66. Write a Python program to calculate body mass index.
hight = float(input("Enter your Hight: "))
weght = float(input("Enter your Weght: "))
BMI = round(weght/(hight*hight),2)
print(BMI)