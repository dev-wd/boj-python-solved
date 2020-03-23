import sys
input = sys.stdin.readline

M = int(input())
card = list(map(int,input().split()))
card.sort()

N = int(input())
test = list(map(int, input().split()))
ans = []
for i in range(N):
  curans = 0
  start = 0
  end = M-1
  while end >= start:
    mid = (start + end) // 2
    if card[mid] < test[i]:
      start = mid + 1
    elif card[mid] > test[i]:
      end = mid - 1
    elif card[mid] == test[i]:
      curans = 1
      break
  ans.append(curans)

for i in range(N):
  print(ans[i], end =' ')
