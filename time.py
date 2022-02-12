#. Write a Python program to display the current date and time.

import datetime as dt
now = dt.datetime.now()
print("Current date")
print("Year:")
print(now.strftime("%d-%m-%Y "))
print("Date:")
print(now.strftime("%H:%M:%S "))
