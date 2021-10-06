# requirements a < b > c OR a  > b < c
# check array of input int on a rolling basis
# 12134 returns 110
# results 100% correct
def isZigzag(numbers):
	array_length = len(numbers)
	# omit arrays less than 3 digits
	if array_length < 3:
		return [0]
	num_groups = array_length - 2
	print(array_length, num_groups)
	current_group = 0
	i = 0
	output = []
	while current_group < num_groups:
		# case 1
		first = numbers[i]
		second = numbers[i+1]
		third = numbers[i+2]
		if (first < second) and (second > third):
			output.append(1)
		elif (first > second) and (second < third):
			output.append(1)
		else:
			output.append(0)
		i+=1
		current_group +=1
	return output

answers = [[1, 1, 0]]
case_dict = {
# case 1: positive missing value
"case1" : [1, 2, 1, 3 , 4],
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
		results = isZigzag(test)
		if (results == answers[i]):
			print("Passed: Test case %s"%str(test))
			i +=1
		else:
			print(("Failed: Test case %s, Expected: %s, Actual: %s" %(str(test), str(answers[i]), str(results))))
			i += 1

run_tests(test_cases,answers)
