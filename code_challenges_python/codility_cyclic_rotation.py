"""
9-2-21
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""

def solution(A,K):
	"""
	Purpose: This function will rotate an array A to the right K times.  Each element in A will be shifted
		right K places.
	:param A: an array
	:param K: # of times to shift elements right
	:return: returns the shifted array
	"""
	# K = 1
	# A = [0,1,2,3]
	# item 0>1, 1>2, 2>3, 3>0 if i+K>len(A) new position = len(A) - i+k
	# create an empty array to store the results
	# this solution is O(N) runtime complexity and O(N*2) storage
	result_array = [None] * len(A)
	# i will be the number of the index
	length_A = len(A)
	for i in range((length_A)):
		shifted_index = i+K
		element_to_shift = A[i]
		# case 1: the shifted_index exceeds the length of the array
		# Therefore, we should start from the beginning
		# case 1a: The shift amount is greater than the array length

		if (shifted_index > length_A-1):
			corrected_index = shifted_index%length_A
			result_array[corrected_index] = element_to_shift
		# case 2: the shift_index is within the array and we can move it directly
		else:
			result_array[shifted_index] = element_to_shift
	return result_array

# k = 4 [8, 9 ,7 ,6, 3]
# k = 5 [3, 8 ,9 ,7,6]
# k = 6 [6,3,8,9,7]
print(solution([3, 8, 9, 7, 6], 5))
