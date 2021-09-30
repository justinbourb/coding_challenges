def solution(input_int):
	"""
	Purpose: This function will accept an int and return the int in reverse order.
			There are two ways to approach this problem that come to mind.
				1) String manipulation (reverse the string then return an int)
				2) reversing the int using only int using powers of ten
			This approach uses purely int. This program works by using powers of 10 and storing each digit in a list.

			Example Input = 123

			# first we find the ints and length of the input
			# first loop
			 x = 123
			 int_list.append(123 % 10) # = 3
			 int_list = [3]
			 x = x//10 (// prevents float)
			# second loop
			 x = 12
			 int_list.append(12 % 10) # = 2
			 int_list = [3, 2]
			 x = x//10 (// prevents float)
			# third loop
			x = 1
			int_list = [3, 2, 1]

			# next we recreate the int in reverse using powers of ten
			# results = (3 * 100) + (2 * 10) + (1 * 1) = 321
	:param input_int: an int
	:return: the int in reverse order
	"""
	int_length = 1
	int_list = []
	return_value = 0
	x = input_int
	pos_input = True
	# track neg inputs, convert to positive value for calculations
	if x<0:
		x = abs(x)
		pos_input = False
	# handle cases where the input is a single digit
	if (x/10<1):
		return x if pos_input else x * -1

	# handle everything else
	while x > 0:
		#check for 1 being the last digit
		if x/10 >= 1:
			int_list.append(x%10)
		else:
			int_list.append(x)
		x = x//10
		int_length +=1

	# recreate the int in reverse order using powers of ten
	for i in int_list:
		current_digit = i
		digit_place = 10**(int_length-2)
		return_value += current_digit * digit_place
		int_length -= 1
	return return_value if pos_input else return_value * -1

case_dict = {
# case 1: positive small single digits
"case1" : 3,
# case 2: positive 1000's digits
"case2" : 1000,
# case 3: positive 100's digits
"case3" : 501,
# case 4: neg small difference
"case4" : -3,
# case 5: neg  1000's digits
"case5" : -1000,
# case 6: neg 100's digits
"case6" : -501,
}

test_cases = []
for key in case_dict:
	test_cases.append(case_dict[key])

answers = [3, 1, 105, -3, -1, -105]

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