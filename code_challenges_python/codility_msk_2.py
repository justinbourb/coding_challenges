# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(S):
	"""
	Given a string of all A or B, find the number of characters that need to be deleted to
	satisfy the rule A must come before B.  All A is acceptable, all B is also acceptable.

	Example:
		Input: 'AAABBB' returns 3, len(A) == len(B) so all A's can be removed or all B's
	Example:
		Input: 'AAAAAAA' returns 0, Input: 'BBBBB' returns 0
	Example:
		Input: 'ABBBABBA' returns ? not sure how to handle this case

	Case 1: # of A > # B, delete some B # return # deleted
	Case 2: # of B > # A, delete some A # return # deleted
	Case 3: no need to delete, A comes before B # return 0
	Case 4: entire string is A or B # return 0
	Case 5: # of B == # of A # return number of A or B

	Return value: # of characters deleted
	"""
	# write your code in Python 3.6
	all_same_chars = True
	previous = S[0]
	A_count = 0
	B_count = 0
	for i in range(1,len(S)):
		# check for Case 4
		if S[i]!=previous:
			all_same_chars = False
		# Case 5
		if S[i] == 'A':
			A_count += 1
		else:
			B_count += 1
	# Case 4
	if (all_same_chars):
		return 0
	# case 5
	if A_count == B_count:
		return A_count
	pass