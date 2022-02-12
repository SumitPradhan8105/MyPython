#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = int(input("Enter a :"))
b = int(input("Enter b :"))
c = int(input("Enter c :"))

if a ==b or b==c or c==a:
    print("Sum: 0")
else:
    print("Sum: ",a+b+c)
