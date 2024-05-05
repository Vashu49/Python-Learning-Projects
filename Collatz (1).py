#!/usr/bin/env python
# coding: utf-8

# In[1]:


def collatz_steps(n):
    if n <= 1:
        return 0

    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1

    return steps

def main():
    n = int(input("Enter a number greater than 1: "))
    if n <= 1:
        print("Number should be greater than 1.")
        return

    steps = collatz_steps(n)
    print(f"Number of steps to reach 1: {steps}")

if __name__ == "__main__":
    main()


# In[ ]:




