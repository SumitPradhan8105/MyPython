#!/usr/bin/env python
# coding: utf-8

# In[23]:


def celtofar(cel):
    far = (cel * 1.8) + 32
    return far
    
def fartocel(far):
    cel = (far - 32) / 1.8
    x = round(cel)
    return x 
    



print("\t Temperature Converter \n ")
print("1. Celcius to farenheit.\n2. Farenheit to Celcius.")
n = int(input("Choice : "))

if n == 1 :
    c = float(input("Enter temperature in celcius : "))
    print(celtofar(c))
elif n == 2 :
    f = float(input("Enter temperature in Farenheit : "))
    print("Temperature in celcius : ",fartocel(f))
else :
    print("Invalid Choice!")              
    


# In[ ]:




