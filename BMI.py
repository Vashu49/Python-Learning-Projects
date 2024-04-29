#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) using weight (in kilograms) and height (in meters).
    Formula: BMI = weight / (height^2)
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret the BMI value and return a corresponding message.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = calculate_bmi(weight, height)
    interpretation = interpret_bmi(bmi)
    
    print(f"Your BMI is {bmi:.2f}, which is considered {interpretation}.")

if __name__ == "__main__":
    main()


# In[ ]:




