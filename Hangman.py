#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def choose_word():
    words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'strawberry', 'watermelon']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess. Attempts left:", attempts)
        else:
            print("Correct guess!")

        print(display_word(word, guessed_letters))

        if '_' not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word:", word)
            break

    if '_' in display_word(word, guessed_letters):
        print("Sorry, you ran out of attempts. The word was:", word)

hangman()


# In[ ]:




