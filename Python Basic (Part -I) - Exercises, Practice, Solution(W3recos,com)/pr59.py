#pro59. Write a Python program to convert height (in feet and inches) to centimeters>
feet = int(input("Feet: "))
inch = int(input("Inch: "))
new_inch = inch + (feet*12)
centimeters = round(new_inch*2.54,1)
print(centimeters, "cm")