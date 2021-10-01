"""
Multiple all the ints in an array to togther and return their sign
Return 1, 0 , -1

Example:
	1. [1,2,3] return 1
	2. [0,1,2] return 0
	3. [-1,-2,-3] return -1
codility results:
100%
"""

def solution(A):
	result = A[0]
	for i in A[1:]:
		result *= i
	if result > 0:
		return 1
	if result < 0:
		return -1
	else:
		return 0

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
