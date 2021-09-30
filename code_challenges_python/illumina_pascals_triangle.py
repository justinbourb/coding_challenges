"""
Pascal's Triangle
Programming challenge description:
A Pascals triangle row is constructed by looking at the previous row and adding the numbers to its left and right to arrive at the new value. If either the number to its left/right is not present, substitute a zero in it's place. More details can be found here: Pascal's triangle. E.g. a Pascal's triangle up to a depth of 6 can be shown as:
          1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5  10   10  5   1
Input:
Your program should read lines from standard input. Each line contains a positive integer which indicates the depth of the triangle (1 based).
Output:
Print out the resulting pascal triangle up to the requested depth in row major form.
Test 1
Test Input
Download Test 1 Input
6
Expected Output
Download Test 1 Input
1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1
"""

import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...
"""
Requirements:
    1) read input string, expect a single digit int
    2) print out a pascal triangle as space separated values
        a) input: 6 expected output: 1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1
"""
"""
Notes:
    print N lines, where N = input #
    line 1 = 1
    line 2 = 1 1
    line 3 = 1 2 1
    line 4 = 1 3 3 1
    line 5 = 1 4 6 4 1
    line 6 = 1 5 10 10 5 1
    line 7 = 1 6 15 20 15 6 1
    line 8 = 1 7 21 35 35 21 7 1
    line 9 = 1 8 28 56 70 56 28 8 1
    sum of each line doubles each time 1, 2, 3, 8, 16, 32, 64, 128
    each line is also powers of 11
"""
"""
Methodology:
    1) Approach 1
        a) check input, concatenate and print that many lines.
        b) there's a limited number of inputs (expect single digit input)
        c) no need to actually calculate pascals triangle
    2) Approach 2
        a) do calculations
        b) take input and use powers of 11 to print each line
        c)  line 1 = 11**0 = 1 
            line 2 = 11**1 = 11
            line 3 = 11**2 = 121
            etc
        d) convert part c into a string and add a space between the digits
"""
for line in sys.stdin:
    print(line, end="")
