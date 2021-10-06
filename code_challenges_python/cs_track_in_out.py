"""
Track if everyone that entered, has left.  Must enter before leaving, cannot enter or exit more than once.
Examples:
	events = [
  ["John_0", "in"],
  ["Mary_0", "in"],
  ["John_0", "out"],
  ["Mary_0", "out"]
]
the output should be shopInAndOutEvents(events) = true.

For

events = [
  ["John_0", "in"],
  ["John_0", "in"],
  ["John_0", "out"],
  ["John_0", "out"]
]
the output should be shopInAndOutEvents(events) = false.

# results: pass 100%
"""

def shopInAndOutEvents(events):
	event_dict = {}
	for i in events:
		key = i[0]
		status = i[1]
		if key in event_dict:
			if event_dict[key][0] == 'in' and status == 'out':
				# allow a person to come in twice, by deleting them from the dict
				del event_dict[key]
			# prevent duplicate in
			elif len(event_dict[key]) > 2:
				return False
			# anything else is False
			else:
				return False
		else:
			if status == 'in':
				event_dict[key] = ['in']
			else:
				return False
	for event in event_dict:
		print(event, len(event))
		if len(event_dict[event]) == 1:
			return False
		if len(event_dict[event]) > 2:
			return False
	# if no False return statements were triggered, return true
	return True

answers = [False, True]
case_dict = {
# case 1: positive missing value
"case1" : [["John_0","in"],
 ["John_1","in"],
 ["John_1","out"]],
# case 2: positive no missing values
"case2" : [["John_0","in"],
 ["Mary_0","in"],
 ["John_0","out"],
 ["Mary_0","out"]],
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
		results = shopInAndOutEvents(test)
		if (results == answers[i]):
			print("Passed: Test case %s"%str(test))
			i +=1
		else:
			print(("Failed: Test case %s, Expected: %s, Actual: %s" %(str(test), str(answers[i]), str(results))))
			i += 1

run_tests(test_cases,answers)