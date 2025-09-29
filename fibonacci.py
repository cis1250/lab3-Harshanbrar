#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

while True:
    print("How many sequences would you like?")
    try:
        sequences = int(input())   # convert input to integer
        print(f'\nYou chose {sequences} sequences')

        if sequences == 0:
            print(0)

        elif sequences > 0:
            a, b = 0, 1
            print("Fibonacci sequence:")
            print(a)
            if sequences > 1:
                print(b)
            for i in range(2, sequences):
                next_term = a + b
                print(next_term)
                a = b
                b = next_term

        else:
            print("\nPlease input a positive number.")

    except ValueError:
        print("\nInvalid input. Please enter a positive integer.")
