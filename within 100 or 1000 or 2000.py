# Write a Python program to test whether a number is within 100 of 1000 or 2000.
n = int(input("Enter number : "))
if n <= 100:
    print(n,"is within 100.")
elif n > 100 and n <= 1000:
    print(n,"is within 100 and 1000.")
elif n > 1000 and n <= 2000:
    print(n,"is within 1000 and 2000.")
else:
    print(n,"lies above 2000")
