#Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
import math

def distance(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

f = (x1,y1)
l = (x2,y2)
print("First Coordinate :",f)
print("Second Coordinate :",l)

print("Distance: ",round(distance(f,l),2))
