#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Order:
    def __init__(self, user):
        self.user = user
        self.items = []
        self.total_price = 0

    def add_to_order(self, product, quantity):
        self.items.append((product, quantity))
        self.total_price += product.price * quantity

    def checkout(self):
        print("Order Summary:")
        for product, quantity in self.items:
            print(f"{product.name} - Quantity: {quantity}, Price: Rs{product.price * quantity}")
        print(f"Total Price: Rs{self.total_price}")
        print("Order placed successfully!")

class InventoryManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                self.products.remove(product)
                print(f"Product '{product_name}' removed successfully.")
                return
        print("Product not found in inventory.")

    def update_stock(self, product_name, quantity):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                product.quantity += quantity
                print(f"Stock of '{product_name}' updated successfully.")
                return
        print("Product not found in inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for product in self.products:
            print(f"Product: {product.name}, Quantity: {product.quantity}, Price: Rs{product.price}")

# Sample usage
if __name__ == "__main__":
    # Creating some sample products
    product1 = Product("Laptop", 800, 10)
    product2 = Product("Printer", 200, 5)
    product3 = Product("Mouse", 20, 20)

    # Creating some sample users
    user1 = User("user1", "user1@example.com")
    user2 = User("user2", "user2@example.com")

    # Creating an inventory manager
    inventory_manager = InventoryManager()

    # Adding products to inventory
    inventory_manager.add_product(product1)
    inventory_manager.add_product(product2)
    inventory_manager.add_product(product3)

    # Displaying inventory
    inventory_manager.display_inventory()

    # Creating an order for user1
    order1 = Order(user1)
    order1.add_to_order(product1, 2)
    order1.add_to_order(product2, 1)
    order1.checkout()

    # Creating an order for user2
    order2 = Order(user2)
    order2.add_to_order(product3, 3)
    order2.checkout()

    # Removing a product from inventory
    inventory_manager.remove_product("Laptop")

    # Updating stock of a product
    inventory_manager.update_stock("Mouse", 10)

    # Displaying updated inventory
    inventory_manager.display_inventory()

