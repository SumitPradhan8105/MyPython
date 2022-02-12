# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference
def double(x):
    print("Diff n - 17: ",x)
n = int(input("Enter the number :"))
if n <= 17 :
    
    print("Diff 17 - n :",17-n)
else :
    double(n-17)
    
