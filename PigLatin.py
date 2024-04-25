#!/usr/bin/env python
# coding: utf-8

# In[2]:


def pig_latin(word):
    vowels = "aeiouAEIOU"
    
    if word[0] not in vowels:
        return word[1:] + "-" + word[0] + "ay"
    else:
        return word + "-ay"

def main():
    word = input("Enter an English word: ")
    pig_latin_word = pig_latin(word)
    print("Pig Latin:", pig_latin_word)

if __name__ == "__main__":
    main()


# In[ ]:




