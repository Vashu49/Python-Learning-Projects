#!/usr/bin/env python
# coding: utf-8

# In[1]:


def number_to_words(num):
    # Define lists for mapping numbers to words
    ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    thousands = [''] + ['Thousand', 'Million']

    # Helper function to recursively convert chunk of three digits to words
    def convert_chunk(n):
        if n == 0:
            return ''
        elif n < 10:
            return ones[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + ('' if n % 10 == 0 else '-' + ones[n % 10])
        else:
            return ones[n // 100] + ' Hundred' + ('' if n % 100 == 0 else ' and ' + convert_chunk(n % 100))

    if num == 0:
        return ones[num]

    words = ''
    chunk_count = 0
    while num > 0:
        chunk = num % 1000
        if chunk != 0:
            chunk_words = convert_chunk(chunk)
            if chunk_count > 0:
                chunk_words += ' ' + thousands[chunk_count]
            if words:
                words = chunk_words + ', ' + words
            else:
                words = chunk_words
        num //= 1000
        chunk_count += 1

    return words

num = int(input("Enter a number (up to one million): "))
print("In words:", number_to_words(num))


# In[ ]:




