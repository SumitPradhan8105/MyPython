#!/usr/bin/env python
# coding: utf-8

# In[9]:


def compound_interest(principle, rate, time):
 
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)
 


P = int(input("Enter Principle :"))
R = float(input("Enter Rate of Interest :"))
T = float(input("Enter time(In years) :"))
print("1. Simple interest \n2.Compund Interest\n")
c = int(input("Enter choice : "))

if c == 1:
    SI = (P*R*T)/100
    print("Simple interest is :",SI)
elif c == 2 :
    compound_interest(P,R,T)
  


# In[ ]:




