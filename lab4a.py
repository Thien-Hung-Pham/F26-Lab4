# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 10/09/2026
# Purpose: Create Simple Functions.
# Usage: ./lab4a.py

# TO DO 1: Add the docstring
# @Function definition: is_even(numbers)
# @param: numbers - a list of integers
# @return: True if any number is even; otherwise, False

# TO DO 2: define the function with name `is_even`.

def is_even(numbers):
	"""Return True if the list contains an even number; otherwise, return False."""
	for number in numbers:
		if number % 2 == 0: # Check if the number is even using modulus operator
			return True
	return False

# TO DO 3: Call the function `is_even`.
result = is_even([1, 3, 5, 7, 8, 9])
print(result)
