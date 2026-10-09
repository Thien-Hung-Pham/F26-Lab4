# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 10/09/2026
# Purpose: Modify the calcualtor program to use keyword parameters.
# Usage: ./lab4e.py

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
    print(f"Result: {compute(num1=num1, num2=num2, operation=operation)}")

    print(compute(operation='+', num2=13, num1=45)) # 45 + 13 = 58
    print(compute(num1=13,operation='*', num2=45)) # 13 * 45 = 585
    print(compute(num2=13, num1=45, operation='/')) # 45 / 13 = 3.46...
    print(compute(num1=13, num2=45, operation='-')) # 13 - 45 = -32
    # Default
    print(compute(num2=13, num1=45)) # 45 + 13 = 58


if __name__ == '__main__':
	main()
