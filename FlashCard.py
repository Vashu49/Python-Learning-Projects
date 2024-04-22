#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Flashcard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

class FlashcardSet:
    def __init__(self, name):
        self.name = name
        self.flashcards = []

    def add_flashcard(self, flashcard):
        self.flashcards.append(flashcard)

    def practice_flashcards(self):
        if not self.flashcards:
            print("No flashcards found in this set.")
            return
        print(f"Practicing Flashcards in Set: {self.name}\n")
        for i, flashcard in enumerate(self.flashcards, start=1):
            print(f"{i}. Term: {flashcard.term}\n   Definition: {flashcard.definition}\n")

# Sample Flashcard sets
set1 = FlashcardSet("Spanish Vocabulary")
set1.add_flashcard(Flashcard("Hola", "Hello"))
set1.add_flashcard(Flashcard("Adiós", "Goodbye"))
set1.add_flashcard(Flashcard("Gato", "Cat"))

set2 = FlashcardSet("French Phrases")
set2.add_flashcard(Flashcard("Bonjour", "Good morning"))
set2.add_flashcard(Flashcard("Merci", "Thank you"))
set2.add_flashcard(Flashcard("Au revoir", "Goodbye"))

# Practice flashcards
set1.practice_flashcards()
set2.practice_flashcards()


# In[ ]:




