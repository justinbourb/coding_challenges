"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
"""

def solution(A):
	answers_dict = {}
	max_num = max(A)
	# create a hash map / dictionary of the items in the array
	for i in range(1, max_num+1):
		answers_dict[i] = False
	# items in A will be marked True
	# missing values will stay False
	for i in A:
		if answers_dict[i] == True:
			# -1 will track items that repeat more than once in an array
			answers_dict[i] = -1
		# do not switch the flag of items that are -1, they repeat in the array
		elif answers_dict[i] == -1:
			continue
		else:
			answers_dict[i] = True
	# check if the answers_dict contains any False values => return 0
	# check if the answers_dict contains any -1 values => return 0
	for key in answers_dict:
		if (answers_dict[key] == False) or (answers_dict[key] == -1):
			return 0
	return 1

case_dict = {
# case 1: each value should appear only once, expect: 0 (3 is twice)
"case1" : [3,1,2,4,3],
# case 2: each value should appear only once, expect: 1
"case2" : [3,1,2,4],
# case 3: each value should be present, expect: 0 (2 is missing)
"case3" : [3,1,4],
# case 4: one value array
"case4" : [1],
# case 5: neg array length = 2
"case5" : [],
# case 6: neg large difference
"case6" : []
}

test_cases = []
for key in case_dict:
	test_cases.append(case_dict[key])

answers = [0, 1, 0, 1]

def run_tests(test_cases, answers):
	results = []
	i = 0
	# prevent out of range errors

	for test in test_cases:
		if (i < len(test_cases) and i < len(answers)):
			# input array, k
			results = solution(test)
			if (results == answers[i]):
				print("Passed: Test case %s"%str(test))
				i +=1
			else:
				print(("Failed: Test case %s, Expected: %s, Actual: %s" %(str(test), str(answers[i]), str(results))))
				i += 1

run_tests(test_cases,answers)