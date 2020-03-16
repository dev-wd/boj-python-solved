import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

m, n = map(int,input().split())
matrix = []
dp = []
for i in range(m):
  tem = input()
  matrix.append([ tem[j] for j in range(n)])
  dp.append([ 0 for j in range(n)])


# bfs
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
def bfs(x, y):
  
  d = deque()
  d.append([x, y, 0])
  cdp = deepcopy(dp)
  cdp[y][x] = 1
  while(d):
    curX, curY, curCount = d.popleft()
    lastNum = curCount
    for i in range(4):
      temX = curX + dx[i]
      temY = curY + dy[i]
      if temX >= 0 and temX < n and temY >= 0 and temY < m and matrix[temY][temX] == 'L' and cdp[temY][temX] == 0:
        d.append([temX, temY, curCount+1])
        cdp[temY][temX] = 1
  return lastNum

ans = 0
# excution
for i in range(m):
  for j in range(n):
    if matrix[i][j] == 'L':
      tem = bfs(j,i)
      ans = max(ans,tem)
      
print(ans)
