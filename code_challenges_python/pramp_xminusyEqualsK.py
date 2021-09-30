'''
Pairs with Specific Difference
Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

Examples:

input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []
Constraints:

[time limit] 5000ms

[input] array.integer arr

0 ≤ arr.length ≤ 100
[input]integer k

k ≥ 0
[output] array.array.integer
'''

''' solution
function
findPairsWithGivenDifference(arr, k):
# since we don't allow duplicates, no pair can satisfy x - 0 = y
if k == 0:
	return []

map = {}
answer = []

for (x in arr):
	map[x - k] = x

for (y in arr):
	if y in map:
		answer.push([map[y], y])

return 
'''


def find_pairs_with_given_difference(arr, k):
	# first I will loop over the array
	# While looping I will store x-k = y in a map / dictionary
	# Then I will loop the array again
	# This time checking if each element is in the array
	# If yes, we have a solution (dict[x], y)
	pair_map = {}
	solutions_array = []
	# first loop O(n)
	for x in arr:
		# x-y = k, therefore x-k = y
		pair_map[x - k] = x
	# second loop O(n)
	for y in arr:
		# check if y is in pair_map
		# O(1), maps are hash tables
		if y in pair_map:
			solutions_array.append([pair_map[y], y])
	return solutions_array


test_cases = [[[4, 1], 3], [[1, 5, 11, 7], 4]]
answers = [[[4, 1]], [[5, 1], [11, 7]]]

def run_tests_two_inputs(test_cases, answers):
	results = []
	i = 0
	for test in test_cases:
		# input array, k
		results = find_pairs_with_given_difference(test[0], test[1])
		if (results == answers[i]):
			print("Passed: Test case %s"%str(test[0]))
			i +=1
		else:
			print(("Failed: Test case %s, Expected: %s, Actual: %s" %(str(test[0]), str(answers[i]), str(results))))
			i += 1

run_tests(test_cases,answers)