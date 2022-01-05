#!/usr/bin/env python
# coding: utf-8

# In[10]:


w = float(input("Enter your weight (in kg) : "))
h = float(input("Enter your height (in cm): "))
h = h/100

bmi = (w / (h*h))

if bmi < 18.5 :
    print("You are Under Weight !")
elif bmi >= 18.5 and bmi <= 24.5 :
    print("You have a Normal Weight !")
elif bmi >= 25 and bmi <= 29.9 :
     print("You are slightly Over-Weight !")
elif bmi >= 30 :
    if bmi >= 30 and bmi <= 34.9 :
         print("You are Obese class 1 !")
    elif bmi >= 35 and bmi <= 39.9 :
         print("You are Obese class 2 !")
    elif bmi >= 40.0 :
         print("You are Obese class 3 !")
else:
    print("Enter the weight and Height properly!")
    
            
    





# In[ ]:





# In[ ]:




