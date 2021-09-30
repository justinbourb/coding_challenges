"""

Given a 2D array binaryMatrix of 0s and 1s, implement a function getNumberOfIslands that returns the number of islands
of 1s in binaryMatrix.

An island is defined as a group of adjacent values that are all 1s. A cell in binaryMatrix is considered adjacent to
another cell if they are next to each either on the same row or column. Note that two values of 1 are not part of the
same island if they’re sharing only a mutual “corner” (i.e. they are diagonally neighbors).

Explain and code the most efficient solution possible and analyze its time and space complexities.

Example:

input:  binaryMatrix = [ [0,    1,    0,    1,    0],
                         [0,    0,    1,    1,    1],
                         [1,    0,    0,    1,    0],
                         [0,    1,    1,    0,    0],
                         [1,    0,    1,    0,    1] ]

output: 6 # since this is the number of islands in binaryMatrix.
          # See all 6 islands color-coded below.
alt

Constraints:

[time limit] 5000ms

[input] array.array.int binaryMatrix

1 ≤ binaryMatrix.length ≤ 100
1 ≤ binaryMatrix[i].length ≤ 100
[output] integer
"""

"""
Peer Solution
def get_number_of_islands(binaryMatrix):
  # requires bfs and dfs to find a value 1
  
  # step 1: loop over matrix to find fist 1
  # step 2:
  # if 1 is found, keep searhing until 0 is found
  # this is the end of the island
  n_islands = 0
  for i in range(len(binaryMatrix)):
    for j in range(len(binaryMatrix[0])):
      if 1 == binaryMatrix[i][j]:
        n_islands += 1
        bfs(binaryMatrix, i, j)
        
        # find island
        
        # 0 0 0
        # 0 0 0
        # 0 0 0
  
  return n_islands


def bfs(binaryMatrix, i, j):
  """
	# Flip 1s to 0s to prevent repeating calculation of islands.
  """
  if 0 == binaryMatrix[i][j]:
    return 
  
  binaryMatrix[i][j] = 0
  
  
  # has upper neighbor
  if 0 < i < len(binaryMatrix):
    bfs(binaryMatrix, i - 1, j)
  
  # has lower neighbor
  if 0 <= i < len(binaryMatrix) - 1:
    bfs(binaryMatrix, i + 1, j)
    
  # has left neighbor
  if 0 < j < len(binaryMatrix[0]):
    bfs(binaryMatrix, i, j - 1)
    
  # has right neighbor
  if 0 <= j < len(binaryMatrix[0]) - 1:
    bfs(binaryMatrix, i, j + 1)
"""



"""
function getNumberOfIslands(binaryMatrix):
    islands = 0
    rows = binaryMatrix.length # number of rows
    cols = binaryMatrix[0].length # number of columns

    for i from 0 to rows-1:
        for j from 0 to cols-1:
            if (binaryMatrix[i][j] == 1):
                markIsland(binaryMatrix, rows, cols, i, j)
                islands++
                
    return islands


function markIsland(binaryMatrix, rows, cols, i, j):
    q = new Queue()
    q.push([i,j])
    while (!q.isEmpty()):
        item = q.pop()
        x = item[0]
        y = item[1]
        if (binaryMatrix[x][y] == 1):
            binaryMatrix[x][y] = -1
            pushIfValid(q, rows, cols, x-1, y)
            pushIfValid(q, rows, cols, x, y-1)
            pushIfValid(q, rows, cols, x+1, y)
            pushIfValid(q, rows, cols, x, y+1)


function pushIfValid(q, rows, cols, x, y):
    if (x >= 0 AND x < rows AND y >= 0 AND y < cols):
        q.push([x,y])

"""