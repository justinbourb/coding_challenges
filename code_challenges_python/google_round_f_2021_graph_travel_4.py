"""
Problem Graph Travel

Ada lives in a magic country A, and she is studying at Magic University. Today, Ada wants to collect magic points in a special space.

The space has N
rooms (0,1,…,N−1). There are M corridors connecting the rooms. A corridor j connects room Xj and room Yj

, meaning you can travel between the two rooms.

The i
-th room contains Ai magic points and is protected by a magic shield with properties Li and Ri. To enter the i-th room, first you need to get to any room adjacent to the i-th room (i.e. connected to it by a corridor) through rooms with already broken shields. Then you have to break the shield to this room, but you can break the shield if and only if you have between Li and Ri magic points, inclusive. After you break the shield, you will enter the room and automatically collect the Ai

magic points assigned to this room. The room will not generate new magic points. The room will also not generate a new shield after it is broken, so you can freely go back to every room with already broken shields regardless of the amount of points you have.

Ada starts with 0
magic points and her goal is to find a way to collect exactly K

magic points. She can start in any room, and end in any room. The room she chooses to start in will automatically have its magic shield broken, and she will automatically collect all the magic points from this room.

After inspecting the map of the rooms and corridors, Ada thinks the task is very easy, so she wants to challenge herself with a more difficult task. She wants to know how many unique ways there are to reach the goal. Two ways are different if their unique paths are different. The unique path is the order of rooms in which she broke the shields, e.g.: if you visit the rooms in the order (1,3,2,1,3,5,3,6)
, the unique path is (1,3,2,5,6)

.
Input

The first line of the input gives the number of test cases, T
. T test cases follow.
For each test case, the first line contains three integers N, M, and K: the number of rooms, the numbers of corridors, and the numbers of magic points we want to collect, respectively.
The next N lines contain three integers Li, Ri, and Ai: The magic shield properties Li and Ri of room i, and the number of magic points Ai, respectively.
The next M lines contain two integers Xj and Yj: the rooms that are connected by corridor j

.
Output

For each test case, output one line containing Case #x
: y, where x is the test case number (starting from 1) and y is the number of ways to collect K

magic points.
Limits

Memory limit: 1 GB.
1≤T≤100
.
0≤M≤N×(N−1)2.
0≤Xj,Yj≤N−1.
Xj≠Yj


Each pair of rooms can be connected by at most one corridor.
Test Set 1

Time limit: 20 seconds.
1≤N≤8
.
1≤K≤100.
0≤Li≤Ri≤50.
1≤Ai≤50

.
Test Set 2

Time limit: 60 seconds.
1≤N≤15
.
1≤K≤2×109.
0≤Li≤Ri≤109.
1≤Ai≤109

.
Sample
Sample Input
save_alt
content_copy

3
4 3 3
1 3 1
1 1 1
2 4 1
2 3 1
0 1
1 2
2 3
4 5 3
1 3 1
1 1 1
2 4 1
2 3 1
0 1
1 2
2 3
3 0
0 2
4 1 2
0 4 1
0 4 1
0 4 2
0 4 2
0 1

Sample Output
save_alt
content_copy

Case #1: 4
Case #2: 8
Case #3: 4

In the first case, there are 4

different ways. They are:
Visualization for the first case, showing 4 different ways.

In the second case, there are 8

different ways. They are:
Visualization for the second case, showing 8 different ways.

In the third case, there are 4
different ways. They are:
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
