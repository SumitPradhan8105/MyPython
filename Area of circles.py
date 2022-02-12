# Write a Python program which accepts the radius of a circle from the user and compute the area. 
from math import pi
r = float(input("Enter Radius of circle:"))
print("Area OF the Circle with radius ",r,"is: ",round(pi*r**2,2))
