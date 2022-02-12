# Write a Python program to calculate number of days between two dates.
from datetime import date
fdate = date(2014,5,7)
ldate = date(2019,5,7)
diff = ldate - fdate
print(diff.days)
