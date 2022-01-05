#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("\tWelcome to pizza station!!\t\t\n")

print("\t\tMENU \t\t\n")

print("1. Mexican Pizza - Rs. 150\n2. American Pizza - Rs 200 \n3. Order Both - Rs 300 \n")
c = int(input("Enter Choice : "))

n = int(input("No. of pizzas :  "))

bill = 0

if c == 1:
    bill = 150 * n
elif c == 2 :
    bill = 200 * n
elif c == 3 : 
    bill = 300 * n
else:
    print ("Thank you for visiting Pizza Station!!")

print("Total Bill : Rs.",bill)


# In[ ]:




