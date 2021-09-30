"""
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
"""

def create_counter(N):
	"""
	Returns a counter array len(N)
	:param N: an Int
	:return: Returns a counter array len(N)
	"""
	return [0]*N

def solution(N, A):
	"""
	See above description.
	:param N: an int representing a counter array.  N should be transformed into an array.
		Example N=5 as input.  Inside the function this turns into the counter array_N =[0, 0, 0, 0, 0]
	:param A: an array of values to compare to the counter.
		1 <= A[i] <= N, array_N[i] += 1
		A[i] = N+1, for i in array_N: i = max(array_N)
		There are no instructions if A[i] > N+1.  Should the function handle this case?
	:return: the updated counter
	"""
	counter = create_counter(N)
	max_counter = 0
	for i in range(0, len(A)):
		# counter operation case 1
		current_value = A[i]
		counter_index = A[i]-1
		if (1 <= current_value and current_value <= N):
			# update the counter at the position given by the value of A[i]-1
			counter[counter_index] += 1
			# check if we should increase max_counter
			if (counter[counter_index] > max_counter):
				max_counter = counter[counter_index]
		# counter operation case 2
		if (current_value == N+1):
			for j in range(0, len(counter)):
				counter[j] = max_counter

	return counter


case_dict = {
	# case 1: positive small difference
	"case1": [5, [3, 4, 4, 6, 1, 4, 4]],
	# case 2: one element
	"case2": [5, [5]],
	# case 3: no path
	"case3": [],
	# case 4: array has all same values
	"case4": [],
	# case 5: neg array length = 2
	"case5": [],
	# case 6: neg large difference
	"case6": []
}

test_cases = []
for key in case_dict:
	test_cases.append(case_dict[key])

answers = [[3, 2, 2, 4, 2], [0, 0, 0, 0, 1]]

def run_tests_two_inputs(test_cases, answers):
	"""
	Runs all test cases to compare actual results to expected results.
	Prints results to console.
	:param test_cases: array with [int, [tests array]]
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