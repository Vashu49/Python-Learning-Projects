#!/usr/bin/env python
# coding: utf-8

# In[2]:


MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char != ' ':
            morse_code += MORSE_CODE_DICT.get(char, '') + ' '
        else:
            morse_code += ' '
    return morse_code.strip()

def morse_to_text(morse_code):
    text = ''
    morse_code += ' '  # Add a space at the end to signify the end of a Morse code sequence
    decoded_chars = morse_code.split(' ')
    for char in decoded_chars:
        if char:
            text += [key for key, value in MORSE_CODE_DICT.items() if value == char][0]
        else:
            text += ' '
    return text

def handle_invalid_input(text):
    # Check if the input text contains only valid characters
    valid_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?:;\'!/()&=@ ')
    return all(char.upper() in valid_chars for char in text)

def handle_invalid_morse_code(morse_code):
    # Check if the input Morse code contains only valid characters
    valid_chars = set('.- ')
    return all(char in valid_chars for char in morse_code)

def main():
    print("Welcome to Morse Code Translator!")
    while True:
        print("\nMenu:")
        print("1. Text to Morse Code")
        print("2. Morse Code to Text")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            text = input("Enter the text to translate to Morse code: ")
            if not handle_invalid_input(text):
                print("Invalid input. Please enter only letters, numbers, and punctuation.")
                continue
            morse_code = text_to_morse(text)
            print("Morse code:", morse_code)
        elif choice == '2':
            morse_code = input("Enter the Morse code to translate to text: ")
            if not handle_invalid_morse_code(morse_code):
                print("Invalid Morse code input. Please enter only dots, dashes, and spaces.")
                continue
            text = morse_to_text(morse_code)
            print("Text:", text)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:




