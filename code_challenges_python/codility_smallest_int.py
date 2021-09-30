'''
Write a function:

class Solution { public int solution(int[] A); }

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
	"""
	Purpose: This function will return the smallest positive integer not in the input array A.
	:param A: N is an integer within the range [1..100,000];
			each element of array A is an integer within the range [−1,000,000..1,000,000].
	:return: the smallest positive integer that does not occur in A
	"""
	max_a = max(A)
	# case 1: max_a is greater than 0, return smallest positive int not in array A
	# This should handle cases were A is not consecutive numbers, max_a+1 is not a valid approach for all cases
	if max_a > 0:
		# case 0: the array is only 1 element long
		if len(A) == 1:
			return A[0]+1
		# remove duplicates for faster processing
		B = set(A)
		# sort for easy comparison
		B = sorted(B)
		# set first item as the min (B is sorted, so this is correct)
		min = B[0]
		gap_value = min
		# if min < 0 we should start searching for gaps at 0
		if (min < 0):
			gap_value = 0

		# skip the first item, since we know it's the current min
		for i in B[1:]:
			# check if numbers in array are consecutive
			if i == gap_value+1:
				gap_value += 1
			# case 1: if we reach the last value, return last value + 1
			# case 1a last value reached and there is a gap value
			elif (i == B[-1] and i != gap_value+1):
				return gap_value+1
			# case 1b: last value reach and there is no gap value
			elif (i == B[-1] and i == gap_value+1):
				return B[-1]+1
			# case 2: if a gap is found, then return gap_value+1 as the smallest integer not in the array
			else:
				return gap_value+1
		return max_a+1
	# case 2: array A has only negative numbers, return 1 for all inputs
	else:
		return 1


# case 1: all int are positive
print(solution([1, 2, 3]))
print("expected: 4")
# return max +1
# case 2: all int are negative
print(solution([-1,-3]))
print("expected: 1")
# return 1
# case 3: all int are the same
print(solution([1,1]))
print("expected: 2")
print(solution([1]))
print("expected: 2")
print(solution([-11]))
print("expected: 1")
# case 5: missing int in array, 6 is max but 5 is not present => 5 is the expected answer
print(solution([1, 3, 6, 4, 1, 2]))
print("expected: 5")

# case 4: int from negative to positive
print(solution([-1, 3]))
print("expected: 1")

"""
9.2.21
Codility does not show test cases or solutions.
Score: 40% correct, 75% performance, Overall 55%
2 out of 5 passing tests, 3 out of 4 performance tests
What is a better solution?
"""