"""
transform a 2d array, rearrange the element diagonally starting from the specified corner
1 | | | 2
  | | |
4 | | | 3
1,2,3,4 specify the corners as above

Examples with in put 1:
	input   abcd  output    acca
			acde			baec
			aeca			ddea

a = [["a", "b", "c", "d"],
     ["a", "c", "d", "e"],
     ["a", "e", "c", "a"]]
and
corner = 1, the output should be

rearrangeOnDiagonals(a, corner) = [["a", "c", "c", "a"],
                                   ["b", "a", "e", "c"],
                                   ["d", "d", "e", "a"]]

Input:
a:
[["a","b","a"],
 ["b","a","b"],
 ["a","b","a"],
 ["b","a","b"],
 ["a","b","a"]]
corner: 4
Output:
null
Expected Output:
[["b","b","a"],
 ["a","a","a"],
 ["b","b","b"],
 ["a","a","a"],
 ["a","b","b"]]

 Input:
a:
[["r","f","l"],
 ["r","v","y"],
 ["l","x","w"],
 ["y","r","u"],
 ["j","v","q"],
 ["u","o","o"]]
corner: 2
Output:
null
Expected Output:
[["r","f","r"],
 ["l","v","l"],
 ["y","x","y"],
 ["j","r","w"],
 ["u","v","u"],
 ["o","o","q"]]

a:
[["a","b","a"],
 ["b","a","b"],
 ["a","b","a"],
 ["b","a","b"],
 ["a","b","a"]]
corner: 3
Output:
null
Expected Output:
[["a","a","b"],
 ["b","a","a"],
 ["b","b","b"],
 ["a","a","b"],
 ["b","a","a"]]
"""

def rearrangeOnDiagonals(a, corner):
	pass

answers = [6, 3, -1, 2]

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
			results = rearrangeOnDiagonals(test[0], test[1])
			if (results == answers[i]):
				print("Passed: Test case %s"%str(test[1]))
				i +=1
			else:
				print(("Failed: Test case %s, Expected: %s, Actual: %s" %(str(test[1]), str(answers[i]), str(results))))
				i += 1

run_tests_two_inputs(test_cases, answers)

