"""
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
"""


def solution_o_n_squared(A):
	"""
	Purpose: See above description
	:param A: an array of 0 and 1 simulating passing cars
	:return: INT, number of pairs of passing cars
	"""
	pairs = 0
	# pairs represented as P,Q. P is the first value and Q the second value.
	# P < Q is a requirement
	# start searching from the beginning of the array
	for i in range(len(A)):
		p = A[i]
		# p must == 0 to search for pairs
		if p==1:
			continue
		else:
			# search through remaining items starting from the next item (i+1) to the end of the array
			# this helps to increase efficiency by not looping through the entire array again
			for j in range(i+1,len(A)):
				q = A[j]
				# case 1: found a pair (p=0 and q=1)
				# increment pairs counter
				if q == 1:
					pairs +=1
				# case 2: a 0 is found.  We should track this position as our next position to search
				# this will prevent us from looping over 1's and will help increase efficiency
				if q == 0:
					next_starting_index = j
			i = next_starting_index


	# requirement: return -1 if pairs > 1 million
	if pairs > 1000000000:
		return -1
	else:
		return pairs

def solution(A):
	"""
	Purpose: See above description
	:param A: an array of 0 and 1 simulating passing cars
	:return: INT, number of pairs of passing cars
	"""
	starting_zero_index = 0
	current_zero_index = 0
	zero_indicies_list = []
	pairs = 0
	# keep track of 0's and calculate pairs at the same time
	for i in range(len(A)):
		if A[i] == 0:
			# update current_zero_index to the value of i
			current_zero_index = i
			# update our pairs count
			index_difference = current_zero_index-(starting_zero_index)
			# if index_difference > 1 then there is at least one match between zeros
			if index_difference > 1:
				pairs += (index_difference-1)*len(zero_indicies_list)
			# update starting index to our current index in preparation for next item in the list
			starting_zero_index = current_zero_index
			# add it to our zero_indicies_list
			zero_indicies_list.append(current_zero_index)
	# check for arrays that end in 1, the for loop does not calculate these trailing 1's
	# so we will do it here
	if A[-1] == 1:
		index_difference = len(A) - current_zero_index
		pairs += (index_difference-1)*len(zero_indicies_list)

	# requirement: return -1 if pairs > 1 million
	if pairs > 1000000000:
		return -1
	else:
		return pairs
case_dict = {
	# case 1: small array ending in 1
	"case1": [0, 1, 0, 1, 1],
	# case 2: small array ending in 0
	"case2": [0, 1, 0, 1, 0],
	# case 3: positive large difference
	"case3": [],
	# case 4: neg small difference
	"case4": [],
	# case 5: neg array length = 2
	"case5": [],
	# case 6: neg large difference
	"case6": []
}

test_cases = []
for key in case_dict:
	test_cases.append(case_dict[key])

answers = [5, 3]


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
			results = solution(test)
			if (results == answers[i]):
				print("Passed: Test case %s"%str(test))
				i +=1
			else:
				print(("Failed: Test case %s, Expected: %s, Actual: %s" %(str(test), str(answers[i]), str(results))))
				i += 1

run_tests(test_cases, answers)
