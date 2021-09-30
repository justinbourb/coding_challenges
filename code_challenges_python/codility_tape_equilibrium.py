"""
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""
def solution(input_array):
	"""
	Purpose: This function will find the minimum difference if an array of int is split into two pieces.
		The difference of the sum of each side must be minimized.  The smallest difference is returned (int).
		Example: returns 1
	:param input_array: an array to find the min difference
	:return: an int, the min difference
	"""
	# first we will find the average of the array.
	# average / 2 = the ideal value to split the array, min difference would be 0
	array_sum = sum(input_array)
	# in the case of a negative array, we take the absolute value of the midpoint
	mid_point = sum(input_array) // 2
	# next we will sort the array to increase the odds of a minimal difference
	# adding small numbers together results in a better split
	sorted_array = sorted(input_array)
	# create left total to keep a tally of the left array
	left_total = 0
	# previous left serve to check the difference at either side of the average
	# by storing the previous value we can check if the left or right side of the average value produces
	# a smaller difference
	previous_left_total = 0
	# keep track if mid_point is negative
	is_mid_point_neg = False

	# if the array is only two elements, return their difference
	if (len(input_array) == 2):
		return input_array[1]-input_array[0]


	# loop over the array until we reach the average
	for num in sorted_array:
		# if the left_total is less than the average, add num to the array
		less_than_mid_point = (left_total<mid_point)
		# for negative mid_points we should flip the comparison
		if (mid_point<0):
			is_mid_point_neg = True
			less_than_mid_point = (mid_point<left_total)

		# for large number spreads, left_total may not pass mid_point until the entire array is added
		# in this case subtract the last num - left_total
		at_last_element = (num == sorted_array[-1])
		if at_last_element:
			return sorted_array[-1] - left_total

		elif less_than_mid_point:
			# keep track of the sum of the left array
			left_total += num
			# check if adding num moved us closer to or further from the mid_point
			# This section also depends if the mid_point is + or -
			if (is_mid_point_neg):
				if ((mid_point-left_total) > (mid_point-previous_left_total)):
					previous_left_total += num
			else:
				if ((mid_point-left_total) < (mid_point-previous_left_total)):
					previous_left_total += num
		else:
			# This assumes right side is larger
			# sum - left_total = right_total, right_total - left_total = 1
			# example: 13 - 6 = 7, 7 - 6 = 1
			right_total = array_sum-left_total
			previous_right_total = array_sum-previous_left_total
			left_diff = right_total - left_total
			left_prev_diff = previous_right_total - previous_left_total
			return min(left_diff, left_prev_diff)
case_dict = {
# case 1: positive small difference
"case1" : [3,1,2,4,3],
# case 2: positive array length = 2
"case2" : [1000, 3000],
# case 3: positive large difference
"case3" : [5000, 100000, 5, 1, 2],
# case 4: neg small difference
"case4" : [-3,-1,-2,-4,-3],
# case 5: neg array length = 2
"case5" : [-1000, -3000],
# case 6: neg large difference
"case6" : [-5000, -100000, -5, -1, -2]
}

test_cases = []
for key in case_dict:
	test_cases.append(case_dict[key])

answers = [1, 2000, 94992, 1, 2000, 94992]

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

run_tests(test_cases,answers)

