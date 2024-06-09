#pro61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.
feet = int(input("Enter distance in feet: "))
inches = feet*12
yards = feet/3
miles = feet/5280.0
print("feet in inches: ",inches )
print("feet in yards: ",yards )
print("feet in miles: ",miles )
