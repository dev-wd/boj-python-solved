import sys
input = sys.stdin.readline
n = int(input())

dp = [100000 for i in range(100001)]
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3

i = 1
while(i**2 < n+1):
  dp[i**2] = 1
  i+=1
for i in range(2,n+1):
  j = 2
  while(j*j <= i):
    dp[i] = min(dp[i],dp[i-j*j]+1)
    j+=1
print(dp[n])
