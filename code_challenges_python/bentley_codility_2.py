"""
biggest value x that occurs x times in the array

methodology:
	max_so_far = 0
	create a dictionary
		dictionary[value] = count
	if dictionary key == count and key > max_so_far:
		max_so_far = key
	return max_so_far

codility results:
100%
"""
def solution(A):
	value_dict = {}
	max_value = 0
	for i in A:
		# if the value is already in the dict, increase the count
		if i in value_dict:
			value_dict[i] += 1
		# else add the value to the dict and set the count to 1
		else:
			value_dict[i] = 1
	# check the dict for matches
	for key in value_dict:
		if key == value_dict[key]:
			if key > max_value:
				max_value = key
	return max_value

answers = [0, 3, 0, 2, 1, 5, 1, 1, 0]
case_dict = {
# case 1: positive missing value
"case1" : [1, 3, 6, 4, 1, 2],
# case 2: positive no missing values
"case2" : [1, 2, 3, 2, 3, 3, 8],
# case 3: negative values
"case3" : [-5, -1, -2],
# case 4: one neg value
"case4" : [2,2],
# case 5: one pos value
"case5" : [1],
# case 6: mixed values missing values
"case6" : [-5000, -100000, 5, 1, 2, 2, 5, 5, 5, 5],
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
			print("Passed: %d Test case %s"%(i,str(test)))
			i +=1
		else:
			print(("Failed: %d Test case %s, Expected: %s, Actual: %s" %(i,str(test), str(answers[i]), str(results))))
			i += 1

run_tests(test_cases,answers)
