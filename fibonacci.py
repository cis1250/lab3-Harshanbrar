#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
while True:
    # Ask the user how many Fibonacci terms they want
    while True:
        print("How many sequences would you like?")
        sequences_input = input()  # user types something (comes in as a string)

    # Check if the input is a number (only digits, no letters or symbols)
        if sequences_input.isdigit():
            sequences = int(sequences_input)  # convert the string to an integer
            break
        else:
            print("Please enter a positive whole number.")  # tell user it was invalid

    # Confirm what the user chose
    print(f"\nYou chose {sequences} sequences.")

    # Case 1: User enters 0 → just print 0
    if sequences == 0:
        print(0)

    # Case 2: User enters a positive number
    elif sequences > 0:
        a, b = 0, 1  # starting values of Fibonacci sequence
        print("Fibonacci sequence:")
        print(a)      # always print first term (0)

        if sequences > 1:
            print(b)  # print the second term (1) if needed

        # Loop to generate the rest of the sequence
        for i in range(2, sequences):  # start at 2 because 0 and 1 are already printed
            next_term = a + b          # add the previous two numbers
            print(next_term)           # show the new term
            a = b                      # move b into a
            b = next_term              # move new term into b

    # Negative numbers are not possible here because .isdigit() blocks them
