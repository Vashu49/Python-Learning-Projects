#!/usr/bin/env python
# coding: utf-8

# In[3]:


def is_valid_credit_card(card_number):
    # Remove any spaces or dashes from the card number
    card_number = card_number.replace(" ", "").replace("-", "")

    # Check if the card number is composed of digits only
    if not card_number.isdigit():
        return False

    # Check if the card number is of valid length for a credit card
    if len(card_number) < 13 or len(card_number) > 19:
        return False

    # Apply Luhn algorithm to validate the card number
    total_sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for i in range(0, num_digits):
        digit = int(card_number[i])

        if not ((i & 1) ^ oddeven):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        total_sum += digit

    return (total_sum % 10) == 0

def detect_credit_card_vendor(card_number):
    # Remove any spaces or dashes from the card number
    card_number = card_number.replace(" ", "").replace("-", "")

    # Check the first few digits to detect the card vendor
    if card_number.startswith("4"):
        return "Visa"
    elif card_number.startswith(("51", "52", "53", "54", "55")):
        return "MasterCard"
    elif card_number.startswith(("34", "37")):
        return "American Express"
    elif card_number.startswith(("6011", "65")):
        return "Discover"
    else:
        return "Unknown"

def main():
    card_number = input("Enter credit card number: ")
    if is_valid_credit_card(card_number):
        vendor = detect_credit_card_vendor(card_number)
        print(f"The credit card number is valid and belongs to {vendor}.")
    else:
        print("Invalid credit card number.")

if __name__ == "__main__":
    main()


# In[ ]:




