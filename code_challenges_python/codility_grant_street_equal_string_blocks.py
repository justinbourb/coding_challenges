"""
Methodology:
	1) loop over string
	2) store current char
	3) if next char == current char, length +=1
	4) if next char != current, all lengths.append(length), length = 0

	5) next loop over lengths and check max_length - length[-i]
	6) return this sum


"""

def solution(S):
	# store first item as current
	previous_char = S[0]
	# start looping from 1
	length = 1
	max_length = 1
	block_list = []
	results = 0
	lenS = len(S)
	for i in range(1,lenS):
		# count length of block
		current_char = S[i]
		if (previous_char == current_char):
			length += 1
			# track max_length for any block found
			if max_length < length:
				max_length = length
		# else append length of previous block to block_list and reset length and current_char
		else:
			block_list.append(length)
			previous_char = current_char
			length = 1
			# check for the last block and add it's length to the list
			if (i == lenS-1):
				block_list.append(length)
	# loop over all block lengths found and calculate the number of chars to add
	for i in block_list:
		# subtract maxlength - length to find additional chars to add
		results += max_length-i
	return results

