import re

def replace_chars(S):
	# remove extra white spaces
	replaced_S = re.sub(' +', ' ', S)
	# replace sentence endings with . for consistency
	# using string.replace due to testing time constraints, using regex would be less code
	replaced_S = replaced_S.replace("! ", ".")
	replaced_S = replaced_S.replace("? ", ".")
	replaced_S = replaced_S.replace(". ", ".")
	replaced_S = replaced_S.replace(" !", ".")
	replaced_S = replaced_S.replace(" ?", ".")
	replaced_S = replaced_S.replace(" .", ".")
	replaced_S = replaced_S.replace("!", ".")
	replaced_S = replaced_S.replace("?", ".")
	return replaced_S

def solution(S):
	# write your code in Python 3.6
	print(S)
	replaced_S = replace_chars(S)
	print(replaced_S)
	split_s = replaced_S.split(".")

	lengths = []
	# find the number of words per sentence
	for i in split_s:
		split_i = i.split(" ")
		lengths.append(len(split_i))
	# return longest sentence
	return max(lengths)




case_dict = {
	# case 1:
	"case1": "We test coders. Give us a try?",
	# case 2:
	"case2": "Forget   CVs..Save Time. x x",
	# case 3:
	"case3": "We !   test coders   . Give us a try   ?",
	# case 4: neg small difference
	"case4": "We    !!!!   test coders   ....  Give us a     try ??!??!?",
	# case 5: neg array length = 2
	"case5": [],
	# case 6: neg large difference
	"case6": []
}

test_cases = []
for key in case_dict:
	test_cases.append(case_dict[key])

answers = [4, 2, 4, 4]


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
