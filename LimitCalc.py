#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sympy import symbols, limit, oo, sympify

def limit_calculator():
    x = symbols('x')

    # Ask the user to enter the function f(x)
    f_x = input("Enter the function f(x): ")

    try:
        # Parse the user input as a SymPy expression
        f_expr = sympify(f_x)

        # Ask the user to enter the limit value
        limit_value = input("Enter the limit value (type 'oo' for infinity): ")

        # Evaluate the limit
        if limit_value.lower() == 'oo':
            lim = limit(f_expr, x, oo)
        else:
            limit_value = float(limit_value)
            lim = limit(f_expr, x, limit_value)

        print("The limit of", f_x, "as x approaches", limit_value, "is:", lim)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    limit_calculator()


# In[ ]:




