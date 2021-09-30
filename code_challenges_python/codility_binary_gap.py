'''
9.1.21
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones
at both ends in the binary representation of N.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if
N doesn't contain a binary gap.


'''

# key = binary number, value = longest binary gap
test_cases = {9:2, 529:4, 20:1, 15:0, 32:0, 1041 : 5, 328:2, 1162:3, 51712:2, 1610612737:28}

def run_tests(test_dict):
	"""
	Purpose: This function tests solution(N)
	:param test_dict: a dictionary of values:results
		example {9:2} 9 will be tested as solution(9) and the expected result is 2
	:return: prints out test results to the console
	"""
	for key in test_dict:
		print(key)
		expected = test_dict[key]
		result = solution(key)

		print("Test " + str(key) + " Expected: " + str(expected) + " Actual: " + str(result) + " Passed: " + str(result == expected) )

def solution(N):
	"""
	This function returns the longest binary gap given an integer N.
	First N is converted into binary, next the largest gap is identified or 0 is returned.
	:param N: an integer N, N is an integer within the range [1..2,147,483,647].
	:return: the largest binary gap or 0
	"""
	binary_N = "{0:b}".format(N)
	starting_one = False
	# count the gap length
	gap_count = 0
	# store all gaps to find the maximum gap length
	all_gaps = []
	for i in (binary_N):
		# toggle starting_one if true a 1 is found
		if i == '1':
			if starting_one == False:
				starting_one = True
			elif starting_one == True:
				# should not toggle starting_one, since a closing_one is also a starting_one of the next gap
				all_gaps.append(gap_count)
				gap_count = 0
		# if a starting 1 is found and i == 0, increase the gap count
		if (i == '0' and starting_one == True):
			gap_count += 1

	if len(all_gaps) == 0:
		return 0
	else:
		return max(all_gaps)

#print(solution(328))
run_tests(test_cases)