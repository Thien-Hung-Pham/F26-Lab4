# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 10/09/2026
# Purpose: Practice variable number of arguments with *args
# Usage: ./lab4f.py

# Follow the instructions from readme.md.


def get_initials(*names): # *names allows for a variable number of arguments to be passed to the function
	"""Return the first letter of each provided name."""
	initials = []
	for name in names:
		initials.append(name[0])
	return initials


def main():
	initials = get_initials("Alice", "Bob", "Charlie", "David")
	print(initials)


if __name__ == "__main__":
	main()
