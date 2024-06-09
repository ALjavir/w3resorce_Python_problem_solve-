#pro13 : Write a program to see the current time
import datetime
now = datetime.datetime.now()
print(now.strftime("%H-%M-%S"))