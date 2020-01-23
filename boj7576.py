import sys
from collections import deque 
input = sys.stdin.readline 

# initiate box
M, N = map(int,input().split())
box = []
for i in range(N):
  box.append(list(map(int,input().split())))

# check tomato
def checkOne():
  stainTomato = deque()
  for i in range(N):
    for j in range(M):
      if box[i][j] == 1:
        stainTomato.append([i,j,0])
  return stainTomato

def checkZero():
  for i in range(N):
    for j in range(M):
      if box[i][j] == 0:
        return True
  return False


# bfs
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

stains = checkOne()
while(1):
  col, row, ans = stains.popleft()
  for i in range(4):
    curCol = col+dy[i]
    curRow = row+dx[i]
    if curCol >= 0 and curCol < N and curRow >=0 and curRow < M and box[curCol][curRow] == 0:
      box[curCol][curRow] = 1
      stains.append([curCol, curRow, ans+1])
  if not stains:
    if checkZero():
      print(-1)
    else:
      print(ans)
    break
