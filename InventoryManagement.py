#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class InventoryManager:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                print(f"Item '{item.name}' removed successfully.")
                return
        print("Item not found in inventory.")

    def update_stock(self, item_name, quantity):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                item.quantity += quantity
                print(f"Stock of '{item.name}' updated successfully.")
                return
        print("Item not found in inventory.")

    def generate_report(self):
        print("Inventory Report:")
        for item in self.items:
            print(f"Item: {item.name}, Quantity: {item.quantity}, Price: Rs{item.price}")

    def set_low_stock_alert(self, threshold):
        for item in self.items:
            if item.quantity < threshold:
                print(f"Alert: Low stock for item '{item.name}'. Quantity: {item.quantity}")

# Sample usage
if __name__ == "__main__":
    inventory_manager = InventoryManager()

    # Adding sample items to inventory
    item1 = Item("Laptop", 10, 800)
    item2 = Item("Printer", 5, 200)
    item3 = Item("Monitor", 8, 150)
    inventory_manager.add_item(item1)
    inventory_manager.add_item(item2)
    inventory_manager.add_item(item3)

    # Remove an item from inventory
    inventory_manager.remove_item("Printer")

    # Update stock of an item
    inventory_manager.update_stock("Laptop", 5)

    # Generate inventory report
    inventory_manager.generate_report()

    # Set up low stock alerts
    inventory_manager.set_low_stock_alert(3)


# In[ ]:




