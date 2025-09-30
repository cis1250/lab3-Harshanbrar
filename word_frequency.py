#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

user_sentence = input("Enter a sentence: ")



while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_input = input("Enter a sentence: ")


# Step 1: Split the sentence into words
list1 = user_sentence.split()

# Step 2: Clean each word
for i in range(len(list1)):
    list1[i] = re.sub(r'[^\w]', '', list1[i])  # remove punctuation
    list1[i] = list1[i].lower()                # make lowercase

# Step 3: Create two empty lists
words = []     # this will hold unique words
freqs = []     # this will hold how many times each word appears

# Step 4: Count the words
for word in list1:
    found = False                # flag to check if word already in words list
    
    # Look through words list to see if word exists
    for j in range(len(words)):
        if words[j] == word:     # word already in the list
            freqs[j] += 1        # increase the count
            found = True
            break
    
    # If word was not found, add it to the list and start count at 1
    if not found:
        words.append(word)
        freqs.append(1)

# Step 5: Print results
for i in range(len(words)):
    print(words[i], ":", freqs[i])
