"""
Problem Festival

You have just heard about a wonderful festival that will last for D
days, numbered from 1 to D. There will be N attractions at the festival. The i-th attraction has a happiness rating of hi and will be available from day si until day ei

, inclusive.

You plan to choose one of the days to attend the festival. On that day, you will choose up to K

attractions to ride. Your total happiness will be the sum of happiness ratings of the attractions you chose to ride.

What is the maximum total happiness you could achieve?
Input

The first line of the input gives the number of test cases, T
. T

test cases follow.

The first line of each test case contains the three integers, D
, N and K. The next N lines describe the attractions. The i-th line contains hi, si and ei

.
Output

For each test case, output one line containing Case #x
: y, where x is the test case number (starting from 1) and y

is the maximum total happiness you could achieve.
Limits

Memory limit: 1 GB.
1≤T≤100
.
1≤K≤N.
1≤si≤ei≤D, for all i.
1≤hi≤3×105, for all i

.
Test Set 1

Time limit: 20 seconds.
1≤N≤1000
.
1≤D≤1000

.
Test Set 2

Time limit: 90 seconds.
For at most 10

test cases:

    1≤N≤3×105

.
1≤D≤3×105

    .


For the remaining cases, 1≤N,D≤1000.

Sample
Sample Input
save_alt
content_copy

2
10 4 2
800 2 8
1500 6 9
200 4 7
400 3 5
5 3 3
400 1 3
500 5 5
300 2 3

Sample Output
save_alt
content_copy

Case #1: 2300
Case #2: 700

In sample test case 1, the festival lasts D=10
days, there are N=4 attractions, and you can ride up to K=2

attractions.

If you choose to attend the festival on the 6th day, you could ride the first and second attractions for a total happiness of 800+1500=2300
. Note that you cannot also ride the third attraction, since you may only ride up to K=2 attractions. This is the maximum total happiness you could achieve, so the answer is 2300

.

In sample test case 2, the festival lasts D=5
days, there are N=3 attractions, and you can ride up to K=3

attractions.

If you choose to attend the festival on the 3rd day, you could ride the first and third attractions for a total happiness of 400+300=700
. This is the maximum total happiness you could achieve, so the answer is 700.
"""


# D days
# N attractions
# hi happiness, Si start date, ei end date
# K which attractions to ride

# output
# sum of happiness rating for attactions in K

# input
# T # of test cases
class Solution:

	def main(self):
		for j in range(int(input())):
			n, p = map(int, input().strip().split())
			l = list(map(int, input().split()))
			print(l)


if __name__ == "__main__":
	Solution.main(input())
