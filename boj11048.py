import sys
input = sys.stdin.readline
sys.setrecursionlimit(40000)
# matrix & dp
n, m = map(int,input().split())
matrix = []
dp = []
for i in range(n):
  matrix.append(list(map(int,input().split())))
  dp.append([-1 for i in range(m)])

# bfs
dx = [-1, -1, 0]
dy = [0, -1, -1]
dp[0][0] = matrix[0][0]
def rec(cy, cx):
  maxVal = -1
  for i in range(3):
    if cy+dy[i] >= 0 and cy+dy[i] < n and cx+dx[i] >= 0 and cx+dx[i] < m:
      temLocationVal = dp[cy+dy[i]][cx+dx[i]]
      if temLocationVal != -1:
        maxVal =  max(maxVal,temLocationVal) 
      else:
        maxVal = max(rec(cy+dy[i],cx+dx[i]), maxVal)
  dp[cy][cx] = maxVal + matrix[cy][cx]
  return dp[cy][cx]

# excution
print(rec(n-1,m-1))
