#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Transaction:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

class FinanceManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def calculate_balance(self):
        balance = 0
        for transaction in self.transactions:
            balance += transaction.amount
        return balance

    def display_transactions(self):
        print("{:<15} {:<20} {:<10}".format("Date", "Description", "Amount"))
        print("-" * 45)
        for transaction in self.transactions:
            print("{:<15} {:<20} ${:<10.2f}".format(transaction.date, transaction.description, transaction.amount))
        print("-" * 45)
        print("Current Balance: ${:.2f}".format(self.calculate_balance()))

def main():
    finance_manager = FinanceManager()

    while True:
        print("\n1. Add Transaction")
        print("2. View Transactions")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter transaction date (YYYY-MM-DD): ")
            description = input("Enter transaction description: ")
            amount = float(input("Enter transaction amount: "))
            transaction = Transaction(date, description, amount)
            finance_manager.add_transaction(transaction)
            print("Transaction added successfully!")

        elif choice == '2':
            finance_manager.display_transactions()

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:




