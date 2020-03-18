import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coin = []
dp = [0 for i in range(k+1)]
dp[0] = 1
for i in range(n):
  coin.append(int(input()))
coin.sort()

for i in range(len(coin)):
  for j in range(1,k+1):
    if coin[i] <= j:
      dp[j] += dp[j-coin[i]]
print(dp[k])
