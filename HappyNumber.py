#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))
    return n == 1

def find_first_n_happy_numbers(n):
    count = 0
    number = 1
    happy_numbers = []
    while count < n:
        if is_happy_number(number):
            happy_numbers.append(number)
            count += 1
        number += 1
    return happy_numbers

first_8_happy_numbers = find_first_n_happy_numbers(8)
print("First 8 Happy Numbers:", first_8_happy_numbers)


# In[ ]:




