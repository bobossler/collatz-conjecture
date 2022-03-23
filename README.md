# collatz-conjecture
Python program testing the Collatz Conjecture, also known as the 3n+1 problem.

## What is the Collatz Conjecture?
The **Collatz Conjecture** is a conjecture in mathematics that concerns a sequence defined as follows: start with a positive integer _n_. Then each item is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of _n_, the sequence will always reach 1.

For more info: [Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture)

## Purpose of the Program
I am writing a program that will confirm that when the Collatz Conjecture is applied to positive integers, the sequence will end with 1. This is not a **proof**. For more information on why the conjecture is not proven, see the link above.

The program flow:
1. Take a starting positive integer
2. Determine if the integer is even or odd
3. If even, divide the integer by 2
4. If odd, multiply the integer by 3 and add 1
5. Check the result: if 1 end, else repeat


## License
____

collatz-conjecture is licensed under the GNU General Public License v3.0 or later

See [LICENSE](LICENSE) to see the full text.

## Things To Do
- Make the program interactive so the user can supply the starting number
- Do more than just print results to screen; maybe write to a file
- Record/store highest integer found in the sequence
- Integrate with a db to catalog all sequneces created


