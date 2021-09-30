import sys

answer_dict = {}
output = ''
for line in sys.stdin:
    # loop over each char
    for letter in line:
        # get the lower case letter
        lower_case_letter = letter.lower()
        # check if lower_case_letter is in the dict
        if lower_case_letter in answer_dict:
            # add 1 to count
            answer_dict[lower_case_letter] += 1
        else:
            # else set the count to 1
            answer_dict[letter] = 1
    # print out the results
    for key in answer_dict:
        output += (str(key) + str(answer_dict[key]))
    # results not yet sorted
    print(output)
    # reset variables for next loop
    output = ''
    answer_dict = {}