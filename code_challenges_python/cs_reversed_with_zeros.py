"""
1) Reverse a number, if any leading zeros once reversed, put them to the end of the number
2) sum all the reversed numbers in an array
Example:
	7 reversed 7
	234 r 432
	58100 r 18500
"""
# results 100% correct

def reverse_i(i):
	# reverse the num as a string
	string_i = str(i)[::-1]
	# check for leading 0 and append to the end
	# don't try to reverse 0, this will create an infinite loop
	if len(string_i) > 1:
		while string_i[0] == '0':
			string_i = string_i[1:] + '0'
	return int(string_i)


def sumOfReversed(arr):
	results = 0
	for i in arr:
		num = reverse_i(i)
		results += num
	return results

answers = [18939]
case_dict = {
# case 1: positive missing value
"case1" : [7, 234, 58100],
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
		results = sumOfReversed(test)
		if (results == answers[i]):
			print("Passed: Test case %s"%str(test))
			i +=1
		else:
			print(("Failed: Test case %s, Expected: %s, Actual: %s" %(str(test), str(answers[i]), str(results))))
			i += 1

run_tests(test_cases,answers)
