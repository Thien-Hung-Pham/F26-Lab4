# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 10/09/2026
# Purpose: use the main Function as entry point.
# Usage: ./lab4c.py

# Follow the instructions from readme.md.


def sum(number1, number2):
	"""Return the sum of two numbers."""
	return number1 + number2


def main():
	"""Read two integers and print their sum."""
	number1 = int(input("Enter the first number: "))
	number2 = int(input("Enter the second number: "))
	total = sum(number1, number2)
	print("The sum is", total)


if __name__ == "__main__": # Check if the script is being run directly (not imported)
	main()
