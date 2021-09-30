"""
Purpose:
    Given a String[] list representing the tasks and an int n, return the task which the businessman chooses
    to execute. A random seed n is provided.  Starting from the first item 1 in the list, we move clockwise
    until n is reached.  n is then dropped from the list and counting starts on the next item after n as item 1.
    This is repeated until there is one item in the list.  The last item is returned.  This is the task chosen.
Input:
    task_list:  1) a string list of tasks from 2-50 elements
                2) each element contains 1-50 characters
                3) each element will contains 'a' - 'z'
    n: an int,  a random positive number
Definition:
    Class:	BusinessTasks
    Method:	getTask
    Parameters:	String[], int
    Returns:	String
    Method signature:	String getTask(String[] list, int n)
    (be sure your method is public)
Return:
    The last item in the list.
"""

class BusinessTasks:
    # instance variable unique to each instance
    def __init__(self, name):
        self.name = name

    def getTask(task_list, random_n):
        counter = 1
        current_index = 0
        for i in task_list:
            if counter == random_n:
                print("removing: " + str(i))
                task_list.remove(i)
                counter = 1
            else:
                counter += 1
        print(task_list)
        return
'''
Questions:
1) How to loop over a list continuously until there is only one element left?
    a) Is a linked list the best option?
    b) Use a while loop to contain the for loop?  While len(list) > 1
2) Tracking the index.
    a) Tracking the index that was dropped so we can start at the next item.
    b) Tracking the index while going from the end of the list to the start of the list
    c) don't track the index, track the number of elements we've gone through instead?
        i) when # of elements = n, drop that item, reset # to 1
'''

if __name__ == '__main__':
    task_list = ["a","b","c","d"]
    n = 2
    # BusinessTasks.getTask(task_list, n)


