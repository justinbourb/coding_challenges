"""
Problem Star Trapper

John and Ada are sitting on the grass above a small hill. It is midnight and the sky is full of stars. The sky looks like a 2D plane from so far away and the stars look like points on that plane. Ada loves blue stars and suddenly she notices one, while all the other stars in the sky are white. She loves the blue star so much that she wants to trap it. And she asks John for help.

Ada will tell John the position of the blue star and he has to trap it. To trap it, John has to draw a polygon in the sky with his buster sword, so that the blue star is strictly inside the polygon (not on the border of the polygon) and the polygon has the smallest possible perimeter. The vertices of the polygon must be the white stars.

Even though John is super awesome, he needs your help. Given the positions of the white stars and the blue star, you need to find out whether John can trap the blue star and if he can, also find the minimum length of the perimeter of the polygon he will use.
Input

The first line of the input gives the number of test cases, T
. T test cases follow.
For each test case, the first line contains an integer N, it denotes the number of white stars in the sky.
The next N lines will each contain two integers, Xi and Yi. The i-th pair of integers denotes the x and y coordinates of the i-th star in the sky.
After these N lines, there will be one last line, which will contain two integers, Xs and Ys

, which denote the x and y coordinates of the blue star.
Output

For each test case, output one line containing Case #x
: y, where x is the test case number (starting from 1) and y is the minimum length of the perimeter of the polygon drawn to trap the shooting star. If it is impossible for John to draw a polygon that traps the star, then y

should be IMPOSSIBLE.

y
will be considered correct if it is within an absolute or relative error of 10−6

of the correct answer. See the FAQ for an explanation of what that means, and what formats of real numbers we accept.
Limits

Memory limit: 1 GB.
1≤T≤100
.
0≤Xi,Yi≤106, for all i.
0≤Xs,Ys≤106

.
No two stars (including the blue star) will have the same position.
Test Set 1

Time limit: 5 seconds.
1≤N≤10

.
Test Set 2

Time limit: 5 seconds.
1≤N≤45

.
Test Set 3

Time limit: 50 seconds.
For at most 10 test cases:
1≤N≤300
.

For the remaining test cases:
1≤N≤60

.
Sample
Sample Input
save_alt
content_copy

2
2
0 0
5 0
2 2
3
0 0
5 0
0 5
1 1

Sample Output
save_alt
content_copy

Case #1: IMPOSSIBLE
Case #2: 17.071068

In the first test case we have only two white stars, so we cannot draw any polygons.

In the second test case we have three white stars, so we can draw only one polygon (a triangle), as shown in the picture below. It turns out that we are able to catch the blue star in this polygon. The length of the perimeter of this polygon is 5+5+52–√≈17.071068
.
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
