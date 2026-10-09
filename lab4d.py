# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 10/09/2026
# Purpose: Create the complete calculator function using default parameters and positional parameters
# Usage: ./lab4d.py

# Follow the instructions from readme.md.


def compute(num1, num2, operation='+'):
	"""Return the result of applying operation to num1 and num2."""
	if operation == '+':
		return num1 + num2
	elif operation == '-':
		return num1 - num2
	elif operation == '*':
		return num1 * num2
	elif operation == '/':
		return num1 / num2
	else:
		return "Invalid operation. Please choose from +, -, *, /."


def main():
	num1 = float(input("Enter the first number: "))
	num2 = float(input("Enter the second number: "))
	operation = input("Choose an operation (+, -, *, /): ")
	print(f"Result: {compute(num1, num2, operation)}")

	print(compute(13, 45, '*'))
	print(compute(13, 45, '/'))
	print(compute(13, 45, '-'))
	print(compute(13, 45, '+'))
	print(compute(13, 45))


if __name__ == '__main__':
	main()
