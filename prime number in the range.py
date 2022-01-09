#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list
 


start = int(input("Enter starting range :"))
end = int(input("Enter Ending range :"))
lst = prime(start,end)

if len(lst) == 0 :
    print("No prime numbers in the range!")
else:
    print("The prime numbers in the range are :",lst)


# In[ ]:




