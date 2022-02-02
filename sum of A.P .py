a = int(input("Please Enter First Number of an A.P Series: : "))
n = int(input("Please Enter number of digits : "))
d = int(input("Please Enter the Common Difference : "))

sum = (n * (2 * a + (n - 1) * d)) / 2
tn = a + (n - 1) * d

print("\nThe Sum of Arithmetic Progression Series = " , sum)
print("The tn Term of Arithmetic Progression Series = " , tn)
