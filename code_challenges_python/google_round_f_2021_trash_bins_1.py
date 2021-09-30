"""
Trash Bins (5pts, 6pts)

Competitive Submissions
Test 1
Completed
00:09:04
remove_red_eye

Last updated: Sep 18 2021, 10:05

Problem

In the city where you live, Kickstartland, there is one particularly long street with N
houses on it. This street has length N, and the N houses are evenly placed along it, that is, the first house is at position 1, the second house is at position 2, and so on. The distance between any pair of houses i and j is |i−j|, where |x| denotes the absolute value of x

.

Some of these houses have trash bins in front of them. That means that the owners of such houses do not have to walk when they want to take their trash out. However, for the owners of houses that do not have trash bins in front of them, they have to walk towards some house that has a trash bin in front of it, either to the left or to the right of their own house.

To save time, every house owner always takes their trash out to the trash bin that is closest to their houses. If there are two trash bins that are both the closest to a house, then the house owner can walk to any of them.

Given the number of houses N

, and the description of which of these houses have trash bins in front of them, find out what is the sum of the distances that each house owner has to walk to take their trashes out. You can assume that at least one house has a trash bin in front of it.
Input

The first line of the input gives the number of test cases, T
. T

test cases follow. Each test case consists of two lines.

The first line of each test case contains an integer N

, denoting the number of houses on the street.

The second line of each test case contains a string S
of length N, representing which houses have trash bins in front of them. If the i-th character in string S is equal to 1, then it means that the i-th house has a trash bin in front of it. Otherwise, if it is equal to 0, then it means that the i

-th house does not have a trash bin in front of it.
Output

For each test case, output one line containing Case #x
: y, where x is the test case number (starting from 1) and y

is the sum of the distances that each house owner has to walk to take their trashes out.
Limits

Time limit: 20 seconds.
Memory limit: 1 GB.
1≤T≤100
.
The length of S is equal to N.
Each character of S is either 0 or 1.
There is at least one character 1 in S

.
Test Set 1

1≤N≤100

.
Test Set 2

1≤N≤5×105

.
Sample

Sample Input
2
3
111
6
100100

Sample Output
Case #1: 0
Case #2: 5
"""

def parse_tests(x):
	"""
	Purpose: this function parses the multiline string input into a list of lists containing the tests.
	format test_list = [[test],[test],[etc]]
	:param x: a multiline input string
	:return: a list of lists format test_list = [[test],[test],[etc]]
	"""
	i = 0
	test = []
	test_list = []
	for line in x.splitlines():
		# the number of tests is irrelevant, skip the first line
		if i==0:
			i+=1
			continue
		# turn the input string into a list of lists
		# format test_list = [[test],[test],[etc]]
		else:
			# length of each test is also irrelevant
			if len(test) < 2:
				test.append(line.strip())
			if len(test) == 2:
				test_list.append(test)
				test = []
	return test_list


def Solution(x):
	test_list = parse_tests(x)
	ones = [-1]
	zero_map = {}
	test_num = 0
	for test in test_list:
		test_num +=1
		length = len(test[1])
		distance_r = 0
		distance_l = 0
		distance = 0
		# loop over each test to evaluate it
		for i in range(length):
			current_char = int(test[1][i])
			last_one = ones[-1]
			if current_char == 1:
				# store the index of ones
				ones.append(i)
			if current_char == 0 and last_one >= 0:
				# distance_r += i - last_one
				distance_calc = i - last_one
				if i in zero_map:
					zero_map[i].append(distance_calc)
				else:
					zero_map[i] = [distance_calc]
		ones=[-1]
		# loop list in reverse
		for i in range( length - 1, -1, -1):
			current_char = int(test[1][i])
			last_one = ones[-1]
			if current_char == 1:
				# store the index of ones
				ones.append(i)
			if current_char == 0 and last_one >= 0:
				# distance_l += last_one - i
				distance_calc = last_one - i
				if i in zero_map:
					zero_map[i].append(distance_calc)
				else:
					zero_map[i] = [distance_calc]

		# find the min distance for each 0
		for key in zero_map:
			# check for two entries in array
			# if two find the min distance
			value_length = len(zero_map[key])
			if value_length == 2:
				left_dist = zero_map[key][0]
				right_dist = zero_map[key][1]
				if left_dist > 0 and right_dist > 0:
					min_value = min(left_dist, right_dist)
					distance += min_value
				elif left_dist > 0:
					distance += left_dist
				elif right_dist > 0:
					distance += right_dist
			# if one entry in array, add that to the distance
			elif value_length == 1:
				left_dist = zero_map[key][0]
				distance += left_dist
		print("Case #" + str(test_num) + ": " + str(distance))



case_dict = {
# case 1: positive small difference
"case1" :
	'''2
	3
	111
	6
	100100'''
,
# case 2: positive array length = 2
"case2" : [],
# case 3: positive large difference
"case3" : [],
# case 4: neg small difference
"case4" : [],
# case 5: neg array length = 2
"case5" : [],
# case 6: neg large difference
"case6" : []
}

test_cases = []
for key in case_dict:
	test_cases.append(case_dict[key])

answers = [[0,5]]

def run_tests(test_cases, answers):
	"""
	Runs all test cases to compare actual results to expected results.
	Prints results to console.
	:param test_cases: array with [[tests array]]
	:param answers: expected answer array
	:return: prints to console
	"""
	results = []
	i = 0
	for test in test_cases:
		# prevent out of range errors
		if (i < len(test_cases) and i < len(answers)):
			results = Solution(test)
			if (results == answers[i]):
				print("Passed: Test case %s"%str(test))
				i +=1
			else:
				print(("Failed: Test case %s, Expected: %s, Actual: %s" %(str(test), str(answers[i]), str(results))))
				i += 1

run_tests(test_cases,answers)
