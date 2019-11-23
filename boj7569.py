import sys
from collections import deque

# input
input = sys.stdin.readline
M, N, H = map(int,input().split())


# matrix
matrix = []
for i in range(H):
  buf2 = []
  for j in range(N):
    buf = list(map(int,input().split()))
    buf2.append(buf)
  matrix.append(buf2)


# dx dy dz
# top bottom left right  zTop zBottom
dx = [ 0, 0, -1, 1, 0, 0]
dy = [ -1, 1, 0, 0, 0, 0]
dz = [ 0, 0, 0, 0, 1, -1]

# bfs
def bfs(listforone):
  ans = 0
  d = deque()
  for i in range(len(listforone)):
    d.append([listforone[i][0],listforone[i][1],listforone[i][2],0])
  
  while(d):
    z, y, x, c = d.popleft()
    ans = max([ans, c])
    for i in range(6):
      tx = x + dx[i]
      ty = y + dy[i]
      tz = z + dz[i]
      if tx < 0 or tx > M-1 or ty < 0 or ty > N-1 or tz < 0 or tz > H-1 : 
        continue
      if matrix[tz][ty][tx] != 0:
        continue
      d.append([tz,ty,tx,c+1])
      matrix[tz][ty][tx] = 1
      
    
  return ans
  
# Buisness logic

List1 = []

# find 1
for h in range(H):
  for n in range(N):
    for m in range(M):
      if matrix[h][n][m] == 1:
        List1.append([h,n,m])
     
# find bfs depth 


realAns = bfs(List1)
  

# find 0

isZero = False
for h in range(H):
  for n in range(N):
    for m in range(M):
      if matrix[h][n][m] == 0:
        isZero = True
        break

if isZero == True:
  print(-1)
else:
  print(realAns)
