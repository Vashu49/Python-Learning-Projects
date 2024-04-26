#!/usr/bin/env python
# coding: utf-8

# In[1]:


def caesar_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_cipher_encrypt(text, key):
    return caesar_cipher(text, key)

def caesar_cipher_decrypt(text, key):
    return caesar_cipher(text, -key)

# Example usage:
plaintext = "HELLO"
key = 3
encrypted_text = caesar_cipher_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)  # Output: "KHOOR"
decrypted_text = caesar_cipher_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)  # Output: "HELLO"


# In[ ]:




