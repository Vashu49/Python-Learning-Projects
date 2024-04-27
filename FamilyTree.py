#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Person:
    def __init__(self, name, birth_year, death_year=None):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        if self.death_year:
            return f"{self.name} ({self.birth_year}-{self.death_year})"
        else:
            return f"{self.name} ({self.birth_year}-)"

def print_tree(person, generation=0):
    print("    " * generation + str(person))
    for child in person.children:
        print_tree(child, generation + 1)

# Example usage
if __name__ == "__main__":
    # Creating people
    john = Person("John", 1950)
    mary = Person("Mary", 1955)
    peter = Person("Peter", 1980)
    sarah = Person("Barack", 1985)
    lisa = Person("Lisa", 1990)

    # Adding children
    john.add_child(peter)
    mary.add_child(peter)
    peter.add_child(sarah)
    peter.add_child(lisa)

    # Printing the tree
    print_tree(john)


# In[ ]:




