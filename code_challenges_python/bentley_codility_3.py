"""
given two lengths A,B construct the largest possible square by dividing the pieces.
leftover pieces are ok

examples:
	1. Given A = 10, B = 21 return 7. 21 / 7 = 3, 10-7 = 1, 3 + 1 =4
	2. Given 13, 11 return 5
	3. Given 2,1 return 0
	4. Given 1,8 return 2
	Expected in put 1 - 1 million

codility results:
75% correct, 71% performance, 73% overall score
"""
def update_dict(i, key, answer_dict):
	if key in answer_dict:
		answer_dict[key] += i
	else:
		answer_dict[key] = i
	return answer_dict

def solution(A,B):
	# find which value is larger
	a_bigger = (A>B)
	possible_answers = []
	max = 0
	if a_bigger:
		largest = A
		smallest = B
	else:
		largest = B
		smallest = A
	larger_pieces = {}
	smaller_pieces = {}
	answer_dict = {}
	for i in range(1,5):
		key = largest // i
		answer_dict = update_dict(i, key, answer_dict)
		key = smallest // i
		answer_dict = update_dict(i, key, answer_dict)
	# answer_dict = {10: 2, 5: 6, 7: 3, 3: 3, 2: 4}

	# check if the smaller piece can be divided into a larger piece
	for key in answer_dict:
		if key < smallest:
			try:
				answer_dict[key] += smallest // key
			except:
				continue
	for key in answer_dict:
		if answer_dict[key] >= 4:
			if key > max:
				max = key
	return max

answers = [7, 5, 0, 2]

case_dict = {
	# case 1: positive small difference
	"case1": [10, 21],
	# case 2: positive array length = 2
	"case2": [13, 11],
	# case 3: no path
	"case3": [2, 1],
	# case 4: array has all same values
	"case4": [1, 8],
	# case 5: neg array length = 2
	"case5": [],
	# case 6: neg large difference
	"case6": []
}

test_cases = []
for key in case_dict:
	test_cases.append(case_dict[key])



def run_tests_two_inputs(test_cases, answers):
	"""
	Runs all test cases to compare actual results to expected results.
	Prints results to console.
	:param test_cases: array with [[tests array], int]
	:param answers: expected answer array
	:return: prints to console
	"""
	results = []
	i = 0
	for test in test_cases:
		# prevent out of range errors
		if (i < len(test_cases) and i < len(answers)):
			# input array, k
			results = solution(test[0], test[1])
			if (results == answers[i]):
				print("Passed: %d, Test case %s"%(i+1, str(test[1])))
				i +=1
			else:
				print(("Failed: %d Test case %s, Expected: %s, Actual: %s" %(i+1, str(test[1]), str(answers[i]), str(results))))
				i += 1

run_tests_two_inputs(test_cases, answers)