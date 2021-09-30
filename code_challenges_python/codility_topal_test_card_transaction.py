"""
 > 0 = bank transfer
 < 0 = credit card, $5 per month
    fee deducted at end of month
    unless there are >=3 card payments per month and >$100
 transactions are recorded in YYYY-MM-DD format

 def solution(A,D)
    A = array of Int representing transactions amounts
    D = array of strings representing transactions dates

 A transaction K is defined as A[K] amount and D[K] date4

"""
def solution(A, D):
	total = 0
	month_map = {
		#map [# of (-) transactions, amount]
	"01":[0,0],
	"02":[0,0],
	"03":[0,0],
	"04":[0,0],
	"05":[0,0],
	"06":[0,0],
	"07":[0,0],
	"08":[0,0],
	"09":[0,0],
	"10":[0,0],
	"11":[0,0],
	"12":[0,0]
	}
	# check transaction total
	for i in A:
		total += i
	# loop through months
	# check dates, check corresponding value for that month
	# if negative add to month dictionary count
	# if count < 3 and amount <100 charge money
	for i in range(len(D)):
		month = D[i].split("-")[1]
		if A[i] < 0:
			# add 1 to the credit transaction count
			month_map[month][0] += 1
			# keep track of total spent
			month_map[month][1] += A[i]
	# remove any monthly fees
	for key in month_map:
		if month_map[key][0] < 3 or month_map[key][1] < 100:
			total -= 5
	return total



case_dict = {
	# case 1:
	"case1": [[100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]],
	# case 2:
	"case2": [[180, -50, -25, -25], ["2020-01-01","2020-01-01","2020-01-01","2020-01-31"]],
	# case 3:
	"case3": [[100, 100, -10, -20, -30], ["2020-01-01","2020-02-01","2020-02-11","2020-02-05","2020-02-08"]],
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

answers = [230,25, 80]

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
			results = solution(test[0], test[1])
			if (results == answers[i]):
				print("Passed: Test case %s"%str(test[1]))
				i +=1
			else:
				print(("Failed: Test case %s, Expected: %s, Actual: %s" %(str(test[1]), str(answers[i]), str(results))))
				i += 1

run_tests_two_inputs(test_cases, answers)
