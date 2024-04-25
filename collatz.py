# collatz.py

# Change Log:
#   Date            Change                                   Who
#  ==================================================================
#  4/22/2024     - removed prompt for starting number
#                  and replaced it with command line
#                  argument parsing using the Standard
#                  Library - argparse
#
#  4/24/2024     - renamed program
#                - added check to prevent starting integer
#                  from being zero or negative
#                - added option to display largest integer
#                  in the list; highest trajectory
#                - added option to display the list
#                  horizontal rather than vertical

import argparse


parser = argparse.ArgumentParser(prog="collatz",
        description="Compute the Collatz-Conjecture",
        epilog="Thanks for using %(prog)s!")

parser.add_argument("integer", metavar="N", type=int,
        help="The starting integer to compute from")

parser.add_argument("-t", "--trajectory", action="store_true",
        help="Display the highest number (trajectory) in the list")

parser.add_argument("-w", "--wide", action="store_true",
        help="Display the list horizontal rather than vertical")

args = parser.parse_args()

# Initialize some variables
steps = 0
highest = 0
out_list = []

# set var = input integer and validate if > 0
x = args.integer
if x <= 0:
    print("The starting integer must be greater than 0")
    raise SystemExit(1)

# Print the starting number
print("Starting number =",x)
print()

# build output list
while x != 1:
    steps += 1
    if x % 2 == 0:
        x /= 2
    else:
        x = x * 3 + 1
    out_list.append(x)
    if x > highest:
        highest = x

if args.wide:
    print(out_list)
else:
    for z in out_list:
        print(z)

print()
print("It took", steps, "steps to reach", x)

if args.trajectory:
    print("The highest number generated was:", highest)
