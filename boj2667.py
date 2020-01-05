import sys
from collections import deque
input = sys.stdin.readline

# bfs
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(row, col):
  numberOfCount = 0
  queue = deque()
  queue.append([row,col])
  matrix[col][row] = 0
  while(queue):
    curRow, curCol = queue.popleft()
    numberOfCount += 1
    for i in range(4):
      tx = curRow + dx[i]
      ty = curCol + dy[i]
      if tx < 0 or tx > n-1 or ty < 0 or ty > n-1 or matrix[ty][tx] == 0 :
        continue
      else:
        matrix[ty][tx] = 0
        queue.append([tx,ty])
  return numberOfCount

# init matrix & answer list
n = int(input())
matrix = []
for i in range(n):
  temInput = input()
  row = [int(temInput[j]) for j in range(n)]
  matrix.append(row)

ansList = []

# iterate matrix 
for i in range(n):
  for j in range(n):
    if matrix[i][j] == 1:
      ansList.append(bfs(j,i))

ansList.sort(reverse=False)
print(len(ansList))
for i in range(len(ansList)):
  print(ansList[i])
