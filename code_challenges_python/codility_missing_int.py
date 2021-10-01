"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

"""
Codility results:
Correctness: 100%, Performance: 100%  Task Score: 100%
"""

def solution(A):
	sorted_A = sorted(A)
	any_missing_values = False
	previous_i = 0
	for i in sorted_A:
		# we're concerned mostly with positive values, though negative is possible
		if i < 0:
			continue
		if i > 0:
			# case 1: check for continuity if true, update the previous value
			if i == previous_i+1:
				previous_i = i
			# case 2: previous_i == i this also counts as no gap
			elif previous_i == i:
				continue
			# case 3: if there is a gap, return previous value +1
			else:
				return previous_i+1
	# if we made it this far there were no gaps in the array and we must check the last item in A
	# this leaves two possibilities
	# case 1: array is full of negative values or ends in 0
	if sorted_A[-1] <= 0:
		return 1
	# case 2: array has at least some positive values without gaps
	if sorted_A[-1] > 0:
		return sorted_A[-1]+1


case_dict = {
# case 1: positive missing value
"case1" : [1, 3, 6, 4, 1, 2],
# case 2: positive no missing values
"case2" : [1, 2, 3],
# case 3: negative values
"case3" : [-5, -1, -2],
# case 4: one neg value
"case4" : [-3],
# case 5: one pos value
"case5" : [1],
# case 6: mixed values missing values
"case6" : [-5000, -100000, 5, 1, 2],
# case 7: mixed values no missing values
"case7" : [-5000, -100000, 3, 1, 2],
# case 8: two gaps
"case8" : [1, 2, 4, 5, 7], # expect 3,
# biggest value is 0
"case9" : [-1,-2,-3,0] #  expect 1
}

test_cases = []
for key in case_dict:
	test_cases.append(case_dict[key])

answers = [5, 4, 1, 1, 2, 3, 4, 3, 1]

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
		# input array, k
		results = solution(test)
		if (results == answers[i]):
			print("Passed: Test case %s"%str(test))
			i +=1
		else:
			print(("Failed: Test case %s, Expected: %s, Actual: %s" %(str(test), str(answers[i]), str(results))))
			i += 1

run_tests(test_cases,answers)

