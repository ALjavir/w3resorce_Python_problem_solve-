#pr3. Write a Python program to display the current date and time.
import datetime
now = datetime.datetime.now()
print(now.strftime("Current date is %y-%m-%d and time is %H-%M-%S"))