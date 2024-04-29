#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import string

def generate_password(length=8, include_upper=True, include_lower=True, include_numbers=True, include_special=True):
    characters = ""
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        print("Error: No character set selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
password = generate_password(length=12, include_upper=True, include_lower=True, include_numbers=True, include_special=True)
print("Generated Password:", password)


# In[ ]:




