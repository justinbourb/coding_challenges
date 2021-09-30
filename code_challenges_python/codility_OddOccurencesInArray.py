'''
9-2-21
Note: Matches are not in any order.
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.

'''

test_cases = [1,2,1,2,3], [1], [1,5,1,2,2], [7, 9, 3, 9, 3, 9, 9, 9, 3, 9, 3, 9, 9, 9, 3, 9, 3, 9, 9, 9, 3, 9, 3, 9, 9, 9, 3, 9, 3, 9, 9, 9, 3, 9, 3, 9, 9]

def solution(A):
	# store the number of occurrences for each element in a dictionary
	dict = {}

	# O(N) looping over array
	for i in A:
		# if the element is already in the dictionary remove it from the possible solutions
		if i in dict:
			try:
				dict[i] += 1
			except:
				pass
		else:
			dict[i] = 1
	# O(N/2) looping over dictionary
	for key in dict:
		if dict[key] == 1:
			return key


print(solution(test_cases[3]))