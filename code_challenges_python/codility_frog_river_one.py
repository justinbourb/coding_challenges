"""
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
"""
# successfully checks if there is a path
# how to test if path is found when possible solution is found
# [3, [3,2,1]]  what is the solution for this??? 3?
# codility challenges are the worst


def solution(X, A):
	answers_dict = {}
	# answers_dict will keep track if a number is seen in the given array
	# all numbers will start as False and be flagged to True when seen in the array
	# If all keys are true, then there is a path
	# If any keys are false, there is not a path
	available_path = False

	for i in range(X+1):
		answers_dict[i] = False

	# toggle keys to true if found in the array
	for i in A:
		answers_dict[i] = True
	# 0 is not in our input set, but is in range(X), set to True to compensate
	answers_dict[0] = True


	# return -1 if any of the keys are still False

	for key in answers_dict:
		if answers_dict[key] == False:
			return -1

	# if there is a path, we should return the index of X
	return A.index(X)


case_dict = {
	# case 1: positive small difference
	"case1": [5, [1, 3, 1, 4, 2, 3, 5, 4]],
	# case 2: positive array length = 2
	"case2": [2, [1, 2]],
	# case 3: no path
	"case3": [6, [1, 3, 1, 4, 2, 3, 5, 4]],
	# case 4: array has all same values
	"case4": [1, [1, 1, 1, 1, 1, 1, 1, 1]],
	# case 5: neg array length = 2
	"case5": [],
	# case 6: neg large difference
	"case6": []
}

test_cases = []
for key in case_dict:
	test_cases.append(case_dict[key])

answers = [6, 3, -1, 2]

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
				print("Passed: Test case %s"%str(test[1]))
				i +=1
			else:
				print(("Failed: Test case %s, Expected: %s, Actual: %s" %(str(test[1]), str(answers[i]), str(results))))
				i += 1

run_tests_two_inputs(test_cases, answers)
