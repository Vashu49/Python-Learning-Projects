#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def flip_coin(num_flips):
    heads = 0
    tails = 0

    for _ in range(num_flips):
        outcome = random.choice(['Heads', 'Tails'])
        if outcome == 'Heads':
            heads += 1
        else:
            tails += 1

    return heads, tails

def main():
    num_flips = int(input("Enter the number of times to flip the coin: "))
    if num_flips <= 0:
        print("Number of flips should be greater than zero.")
        return

    heads, tails = flip_coin(num_flips)

    print(f"Number of Heads: {heads}")
    print(f"Number of Tails: {tails}")

if __name__ == "__main__":
    main()


# In[ ]:




