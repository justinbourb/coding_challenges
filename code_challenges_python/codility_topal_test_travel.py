"""
 photo extensions .jpg, .png, .jpeg
 format
    photo, city, date, time
    "photo.jpg, Warsaw, 2013-09-05 14:08:15"
    Photos may share the same time and date due to timezone differences
 group photos by city -> sort by time -> assign consecutive numbers 1-N to each photo
    each number should have the same length = the longest number in each group
    example: min = 000000001, max = 10000000
 photo extensions should remain the same

 Example input:
    photo.jpg, Warsaw, 2013-09-05 14:08:15
    john.png, London, 2015-06-20 15:13:22
    myFriends.png, Warsaw, 2013-09-05 14:07:13
 Example output:
    Warsaw02.jpg
    Long1.png
    Warsaw01.jpg
 The new names of the photos are returned in the same order as the input string.

 Input is a string or array, output is a string

"""

def solution(S):
	photo_map = {}
	#step 1: split input by \n to separate each photo
	# for string inputs
	try:
		photos_list = S.split("\n")
	# for array / list inputs
	except:
		photos_list = S[0].split("\n")
	#step 2: store as a map to save position in input so output can be in the same order
		#photo_map{city: [[input_index, input_string_text, order_within_city]]}
	for i in range(len(photos_list)):
		city = photos_list[i].split(",")[1]
		city = city.strip()
		# check if the key has been created
		if city in photo_map:
			photo_map[city].append([i, photos_list[i]])
		# else create the key
		else:
			photo_map[city] = []
	#step 3: loop over each items for each city in the photo_map to determine their order
		#record the order in the map
	for key in photo_map:
		# for each key loop over the list for that key to evalute each photo in the grouping
		for i in photo_map[key]:
			# photo_map[key=city][i=item_in_list][1=input_string]
			date = photo_map[key][i][1].split(",")[2]
			time = photo_map[key][i][1].split(",")[3]

			# how to sort dates
			# option 1:
			# bucket sort
			# create a map with years as buckets
			"""
			sub_items_map{
			2013:,
			2016:,
			etc
			}
			"""
			# each year would have a sub-bucket for month and day?

			# option 2:
			# research how to sort dates in python (this is the better method)
			# sorting dates is often rather complicated and requires specific implementations per language
			# else odd results will occur
	#step 4: find the length of the largest number in each city
		#then prepend leading 0's for any number that is a shorter length
	"""
	Psuedocode:
	desired_length = max(number_length)
	for numbers in city:
		While numbers < desired_length:
			prepend 0 
	"""
	#step 5: return the results in the same order based on the photo_map input_index
	"""
	return results in order based on recorded input_index
	"""
	pass


case_dict = {
	# case 1:
	"case1": 'photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\nmyFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\ng.jpg, Warsaw, 2016-02-29 22:13:11',
	# case 2:
	"case2": ['photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\nmyFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\ng.jpg, Warsaw, 2016-02-29 22:13:11'],
	# case 3:
	"case3": "",
	# case 4: neg small difference
	"case4": [],
	# case 5: neg array length = 2
	"case5": [],
	# case 6: neg large difference
	"case6": []
}

test_cases = []
for key in case_dict:
	test_cases.append(case_dict[key])

answers = [4, 2]


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

run_tests(test_cases, answers)