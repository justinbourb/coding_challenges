def gen_blank_array(length):
	blank_array = []
	temp = []
	for i in range(length):
		temp.append(0)
	for i in range(length):
		# append a shallow copy, if just append is used, all arrays will point to the same array
		# modifying one would modify all of them
		blank_array.append(temp[:])
	return blank_array

def solution_using_new_array(arr):
	"""
	This function will rotate a 2d array 90 degrees clockwise.
	This is accomplished by filling in a blank array with the data provided as input.
	:param arr: an array of numbers to rotate
	:return: a new rotated array
	"""
	blank_array = gen_blank_array(len(arr))
	# first row => arr[len(arr)-1][i]
	# second row => arr[len(arr)-2][i]
	row = 1
	max_index = len(arr)
	for i in range(max_index):
		for j in range(len(arr[i])):
			calculated_row = j
			calculated_column = max_index-row
			value_to_transpose = arr[i][j]
			blank_array[calculated_row][calculated_column] = value_to_transpose
		row +=1
	return blank_array

def solution(arr):
	"""
	Purpose:
		This function will rotate a 2d array 90 degrees clockwise.
		This is accomplished by modifying the provided array in place.
	Methodology:
		1) Convert the rows into columns by swapping values horizontally.
			Each row in the diagram is a list of values.
			[1     [1 2 3 4 5]
			 2  =>
			 3
			 4
			 5]
		2) Swap columns into the correct order
			[1 2 3 4 5] => [5 2 3 4 1] => [5 4 3 2 1]
	:param arr: an array of numbers to rotate
	:return: a the input array rotated in place
	"""
	height = len(arr)
	width = len(arr[0])
	# Step 1 convert rows into columns
	# swap from height 0 to N-1
	# swap from width 0 to N-1
	# i and j are int
	for i in height:
		for j in width:
			pass


answers = [[
	[13,9,5,1],
	[14,10,6,2],
	[15,11,7,3],
	[16,12,8,4]
],
[
	[7,4,1],
	[8,5,2],
	[9,6,3]
]]
case_dict = {
# case 1: positive missing value
"case1" : [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[13,14,15,16]
           ],
# case 2: positive no missing values
"case2" : [
	[1,2,3],
	[4,5,6],
	[7,8,9]
           ],
# case 3: negative values
"case3" : [-5, -1, -2],
# case 4: one neg value
"case4" : [-3],
# case 5: one pos value
"case5" : [1],
# case 6: mixed values missing values
"case6" : [-5000, -100000, 5, 1, 2],
# case 7: mixed values no missing values
"case7" : [-5000, -100000, 3, 1, 2],
# case 8: two gaps
"case8" : [1, 2, 4, 5, 7], # expect 3,
# biggest value is 0
"case9" : [-1,-2,-3,0] #  expect 1
}

test_cases = []
for key in case_dict:
	test_cases.append(case_dict[key])



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
	test_limit = min(len(answers), len(test_cases))

	for test in test_cases:
			# input array, k
			# ensure each test has a answer, or each answer has a test
		if (i < test_limit):
			results = solution(test)
			if (results == answers[i]):
				print("Passed: Test case %s"%str(test))
				i +=1
			else:
				print(("Failed: Test case %s, Expected: %s, Actual: %s" %(str(test), str(answers[i]), str(results))))
				i += 1

run_tests(test_cases,answers)
