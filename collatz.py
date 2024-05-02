""" collatz.py
A small test program to do the math of the Collatz-Conjecture

Change Log:
Date            Change                                   Who
==================================================================
4/22/2024     - removed prompt for starting number
                and replaced it with command line
                argument parsing using the Standard
                Library - argparse

4/24/2024     - renamed program
              - added check to prevent starting integer
                from being zero or negative
              - added option to display largest integer
                in the list; highest trajectory
              - added option to display the list
                horizontal rather than vertical

5/1/2024      - removed regular comments at the top and
                replaced them with a docstring
              - changed the division symbol (/) with an
                integer division (//) to keep the output
                as integer instead of floating
              - refactored code and placed main work in
                a function
"""
import argparse


def gen_collatz(the_num):
    """ gen_collatz function
    takes a starting integer and then computes an output list
    using the Collatz-Conjecture method
    """
    step_cnt = 0
    high_num = 0
    out_list = []

    # build output list
    while the_num != 1:
        step_cnt += 1
        if the_num % 2 == 0:
            the_num //= 2
        else:
            the_num = the_num * 3 + 1
        out_list.append(the_num)
        if the_num > high_num:
            high_num = the_num
    return out_list, high_num, step_cnt


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

# validate nput integer is > 0
if args.integer <= 0:
    print("The starting integer must be greater than 0")
    raise SystemExit(1)

# Print the starting number
print("Starting number =",args.integer)
print()
(collatz_list, high_traj, steps) = gen_collatz(args.integer)

if args.wide:
    print(collatz_list)
else:
    for z in collatz_list:
        print(z)

print()
print("It took", steps, "steps to reach", args.integer)

if args.trajectory:
    print("The highest number generated was:", high_traj)
