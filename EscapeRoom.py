#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time

class Room:
    def __init__(self, name, description, puzzles, locked=True):
        self.name = name
        self.description = description
        self.puzzles = puzzles
        self.locked = locked

    def enter_room(self, inventory):
        print("\n---", self.name, "---")
        print(self.description)
        if self.locked:
            print("This room is locked!")
            return False
        else:
            for puzzle in self.puzzles:
                if not puzzle.solve(inventory):
                    print("You failed to solve the puzzle. GAME OVER!")
                    return False
            print("Congratulations! You solved all the puzzles in the room.")
            return True

class Puzzle:
    def __init__(self, question, answer, required_item=None):
        self.question = question
        self.answer = answer
        self.required_item = required_item

    def solve(self, inventory):
        print("\n--- Puzzle ---")
        print(self.question)
        if self.required_item:
            if self.required_item in inventory:
                print("You use the", self.required_item, "to solve the puzzle.")
            else:
                print("You need a", self.required_item, "to solve this puzzle.")
                return False
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == self.answer:
            print("Correct!")
            return True
        else:
            print("Incorrect!")
            return False

def main():
    # Define puzzles and items
    key = "key"
    key_location = "under the mat"
    room1_puzzles = [Puzzle("What is the capital of France?", "paris")]
    room1 = Room("Entrance Hall", "You are in a dimly lit entrance hall.", room1_puzzles, locked=False)

    room2_puzzles = [Puzzle("What is the result of 2 + 2?", "4", required_item=key)]
    room2 = Room("Library", "You are in a dusty old library.", room2_puzzles)

    # Start the game
    print("Welcome to the Escape Room Game!")
    time.sleep(1)
    print("You find yourself trapped in a mysterious mansion.")
    time.sleep(1)
    print("Your objective is to solve puzzles in each room to escape.")
    time.sleep(1)

    # Initialize inventory
    inventory = []

    # Enter rooms
    if room1.enter_room(inventory):
        inventory.append(key)
        print("You found a key!")
        print("You add the key to your inventory.")
        time.sleep(1)
        print("You exit the room and continue exploring the mansion.")

        # Unlock room 2
        room2.locked = False
        if room2.enter_room(inventory):
            print("Congratulations! You escaped from the mansion.")

if __name__ == "__main__":
    main()


# In[ ]:




