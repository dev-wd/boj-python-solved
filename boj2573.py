import sys
from collections import deque
import copy
input = sys.stdin.readline

# make matrix
N, M = map(int, input().split())
matrix = []
for i in range(N):
  matrix.append(list(map(int,input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# remove ice
def removeIce(x, y):
  count = 0
  for i in range(4):
    curX = x+dx[i]
    curY = y+dy[i]
    if curX >=0 and curX <= M-1 and curY >= 0 and curY <= N-1 and temMatrix[curY][curX] == 0:
      count += 1
  if  temMatrix[y][x] - count < 0:
    tem2Matrix[y][x] = 0
  else:
    tem2Matrix[y][x] = tem2Matrix[y][x] - count
  
# check ice count by bfs
def checkIceCountBFS(x,y,curMatrix):
  q = deque()
  q.append([x, y])
  curMatrix[y][x] = 0
  while(q):
    curX, curY = q.popleft()
    for i in range(4):
      nextX = curX + dx[i]
      nextY = curY + dy[i]
      if nextX >=0 and nextX <= M-1 and nextY >= 0 and nextY <= N-1 and curMatrix[nextY][nextX] != 0:
        curMatrix[nextY][nextX] = 0
        q.append([nextX, nextY])
  return curMatrix 

year = 0
temMatrix = matrix
while(1):
  # logic for count
  count = 0
  tem3Matrix = copy.deepcopy(temMatrix)
  for j in range(N):
    for k in range(M):
      if tem3Matrix[j][k] == 0:
        continue
      count += 1
      tem3Matrix = checkIceCountBFS(k,j,tem3Matrix)
  year += 1
  # check answer
  if count == 0:
    print(0)
    break
  elif count >= 2:
    print(year-1)
    break
  # logic for years
  tem2Matrix = copy.deepcopy(temMatrix)
  for j in range(N):
    for k in range(M):
      if temMatrix[j][k] != 0:
        removeIce(k,j)
  temMatrix = tem2Matrix
