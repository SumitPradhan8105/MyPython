#Write a Python program to print the calendar of a given month and year.

#Note: Use 'calendar' module.

import calendar
y = int(input("Enter Year : "))
m = int(input("Enter Month : "))
print(calendar.month(y,m))
