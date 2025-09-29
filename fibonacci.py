#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

while True:  
    # Ask the user how many Fibonacci terms they want
    print("How many sequences would you like?")

    try:
        # Convert input to an integer (input() gives a string by default)
        sequences = int(input())
        print(f'\nYou chose {sequences} sequences.')

        # Case 1: User enters 0 → just print 0
        if sequences == 0:
            print(0)

        # Case 2: User enters a positive number
        elif sequences > 0:
            a, b = 0, 1  # starting values of Fibonacci sequence
            print("Fibonacci sequence:")
            print(a)      # always print first term
            if sequences > 1:
                print(b)  # print second term if needed

            # Loop to generate remaining terms
            for i in range(2, sequences):
                next_term = a + b  # add previous two numbers
                print(next_term)
                a = b              # shift values forward
                b = next_term

        # Case 3: User enters a negative number
        else:
            print("\nPlease input a positive number.")

    except ValueError:
        # Handles case where user enters something not a number (e.g., "hello")
        print("\nInvalid input. Please enter a positive integer.")
