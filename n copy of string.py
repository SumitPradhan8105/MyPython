#Write a Python program to get a string which is n (non-negative integer) copies of a given string.
def calc(str,x):
    result = ""
    for i in range(x):
        result = result+str
    print(result)    

string = input("Input String : ")
n = int(input("Enter number of Repetitions :"))
if n < 0:
    print("Negative")
else : 
    calc(string,n)
