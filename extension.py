#Write a Python program to accept a filename from the user and print the extension of that. 
filename = input("Input file name:")
fname = filename.split('.')
print("Extension : ",fname[-1])
