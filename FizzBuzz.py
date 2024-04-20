#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Test the function with numbers from 1 to 100
fizz_buzz(100)


# In[ ]:




