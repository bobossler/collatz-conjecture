# Collatz_Conjecture.py

# last modified: 4/22/2024
# Changes: removed prompt for starting number and
#          replaced it with command line argument
#          parsing using the Standard Library - argparse

import argparse

parser = argparse.ArgumentParser(description='Compute the Collatz-Conjecture')

parser.add_argument('integer', metavar='N', type=int,
        help='The starting integer to compute from')

args = parser.parse_args()

# Initialize iterator
i = 0

# set var to = the input parameter
x = args.integer

# Print the starting number
print ("Starting number =", x)

# Start main loop
while x != 1:
    i += 1
    if x % 2 == 0:
        x /= 2
    else:
        x = x * 3 + 1
    print (x)

print ("It took", i, "steps to reach", x)
