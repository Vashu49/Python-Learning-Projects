#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Flower:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def order_more(self, quantity):
        print(f"Ordering {quantity} more {self.name} flowers...")
        self.quantity += quantity

    def sell(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            print(f"Sold {quantity} {self.name} flowers.")
        else:
            print(f"We don't have enough {self.name} flowers in stock.")

class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower, quantity):
        self.flowers.append((flower, quantity))

    def sell(self):
        total_price = 0
        for flower, quantity in self.flowers:
            if flower.quantity >= quantity:
                total_price += flower.price * quantity
                flower.sell(quantity)
            else:
                print(f"We don't have enough {flower.name} flowers in stock to complete the bouquet.")
                return
        print(f"Bouquet sold for Rs{total_price}.")

# Creating flower objects
rose = Flower("Rose", 2, 10)
lily = Flower("Lily", 3, 5)

# Creating bouquet object
bouquet = Bouquet()
bouquet.add_flower(rose, 6)
bouquet.add_flower(lily, 4)

# Selling the bouquet
bouquet.sell()

# Ordering more flowers
rose.order_more(5)

# Trying to sell the bouquet again
bouquet.sell()


# In[ ]:




