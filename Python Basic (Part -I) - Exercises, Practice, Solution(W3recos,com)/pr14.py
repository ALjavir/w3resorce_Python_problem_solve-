#pro 14. Write a Python program to calculate number of days between two dates.
from datetime import date
date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)
date_count = date1-date2
print(date_count.days)