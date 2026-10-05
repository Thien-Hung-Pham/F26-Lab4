# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date:
# Purpose: Create Some Complex Functions.
# Usage: ./lab4b.py

# TO DO 1: Add the docstring
# @Function definition: even_numbers(numbers)
# @param: numbers - a list of integers
# @return: Returns a new list of all the even numbers from the list

# TO DO 2: Create the function.
def even_numbers(numbers):
    """Return a new list containing the even numbers from numbers."""
    new = []
    for number in numbers:
        if number % 2 == 0:
            new.append(number)
    return new

# TO DO 3: Call the function.
result = even_numbers([1, 2, 3, 4, 5, 6, 7, 8])
print(result)
