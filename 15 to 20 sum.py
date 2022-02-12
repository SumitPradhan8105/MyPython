#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return
a = int(input("Enter a :"))
b = int(input("Enter b :"))
sum = a+b

if 15 <= sum <= 20:
    print("Sum :",sum)
else:
    print("Sum is not between 15 to 20")
