#Write a Python program to count a specific number in a given list.
count = 0
n = int(input("Enter the number to find :"))

lst = []
size = int(input("Enter the size of the list : "))
for i in range(0,size):
    temp = int(input())
    lst.append(temp)
print(lst)
count = 0
for num in lst:
    if num == n:
        count = count + 1
print("Count : ",count)
