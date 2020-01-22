import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

M, N = map(int,input().split())

dp = []
numberMap = []
for i in range(M):
  numberMap.append(list(map(int,input().split())))
  dp.append([-1 for j in range(N)])
dp[0][0] = 1

def rec(row,col):
  if dp[col][row] != -1:
    return dp[col][row]
  else:
    dp[col][row] = 0
  tm1 = 0
  tm2 = 0
  tm3 = 0
  tm4 = 0
  if col - 1 >= 0 and (numberMap[col][row]<numberMap[col-1][row]):
    tm1 = rec(row,col-1)
  if row - 1 >= 0 and (numberMap[col][row]<numberMap[col][row-1]):
    tm2 = rec(row-1,col)
  if row + 1 < N and (numberMap[col][row]<numberMap[col][row+1]):
    tm3 = rec(row+1,col)
  if col + 1 < M and (numberMap[col][row]<numberMap[col+1][row]):
    tm4 = rec(row,col+1)
  dp[col][row] = tm1+tm2+tm3+tm4
  return dp[col][row]

print(rec(N-1,M-1))
