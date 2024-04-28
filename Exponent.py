#!/usr/bin/env python
# coding: utf-8

# In[1]:


def power(a, b):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2
    return result

a = int(input("Enter base (a): "))
b = int(input("Enter exponent (b): "))

print("Result:", power(a, b))


# In[ ]:




