def solution(S):
	"""
	Given a string, find the longest balanced section of the string.
	Requirements:
	    1) upper and lower case version of the letter must be present
	    2) no other characters can break the substring
	    Example:
			Input: 'azABaabza'  Returns: 5 from substring 'ABaab'

	My solution is missing a way to track the longest balanced fragment.
	Currently is checks if both upper and lower case characters are in the string.
	TODO: check for longest balanced fragment
	    1) track letters found. lower or uppercase okay. if letter match not found, it's a break

	Running in O(N) time and space complexity.
	:param S:
	:return:
	"""
	# key = letter: [0 = upper case present, 1 = lower case present]
	answer_map = {
	}
	balanced = 0
	# create the map
	for i in S:
		key = i.lower()
		if key in answer_map:
			continue
		else:
			answer_map[key] = [False,False]
	# fill in the map
	for i in S:
		key = i.lower()
		if i.islower():
			# 0 is upper
			# 1 is lower
			answer_map[key][1] = True
		else:
			answer_map[key][0] = True
	# check for both
	for key in answer_map:
		# if lower and upper case have been toggled true, continue checking
		if answer_map[key][0] == True and answer_map[key][1] == True:
				balanced += 1
	if balanced > 0:
		return balanced
	else:
		return -1

print(solution('azABaabza'))
print(solution('asdfsafdsafs'))
print(solution('TacoCat'))