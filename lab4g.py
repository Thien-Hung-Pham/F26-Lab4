# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 10/09/2026
# Purpose: Practice map, filter and lambda expressions.
# Usage: ./lab4g.py

# Follow the instructions from readme.md.

# Create numbers from 2 through 10, then square each value using map and lambda.
numbers = list(range(2, 11))
numbers = list(map(lambda number: number ** 2, numbers))
print(numbers)

# Filter the squared numbers to keep only values divisible by 2.
divisible_by_2 = list(filter(lambda number: number % 2 == 0, numbers))
print(divisible_by_2)
