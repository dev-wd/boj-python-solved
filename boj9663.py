import sys
import copy
from collections import deque
input = sys.stdin.readline

# make matrix
N = int(input())
matrix = []
for i in range(N):
  matrix.append([ 0 for j in range(N)])

# draw line of queen
def lineQueen(row,col,matrix):
  matrix[col][row] = 1
  for i in range(N):
    matrix[i][row] = 1
    matrix[col][i] = 1
    if col-i >= 0 and row-i >= 0 :
      matrix[col-i][row-i] = 1
    if col+i <= N-1 and row+i <= N-1:
      matrix[col+i][row+i] = 1
    if col+i <= N-1 and row-i >= 0:
      matrix[col+i][row-i] = 1
    if col-i >= 0 and row+i <= N-1:
      matrix[col-i][row+i] = 1
  return matrix
# dfs 
def dfs(row, col):
  temMatrix = matrix
  count = 0
  stack = deque()
  stack.append([row,col,temMatrix])
  # how to erase line... when go back
  while(stack):
    curRow, curCol, temMatrix = stack.pop()
    temMatrix = lineQueen(curRow,curCol,copy.deepcopy(temMatrix))
    curCol +=1
    for i in range(N):
      if temMatrix[curCol][i] == 0:
        if curCol == N-1:
          count+=1
        else:
          stack.append([i,copy.deepcopy(curCol),copy.deepcopy(temMatrix)])
  return count
# excute tree of dfs
answer = 0 
for i in range(N):
  answer += dfs(i,0)
print(answer)
