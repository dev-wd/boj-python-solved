import sys
input = sys.stdin.readline

# input
N = int(input())
ask = list(map(int, input().split()))
total = int(input())
ask.sort()

# is correct
def isCorrect(limit):
  temTotal = 0
  for i in range(N):
    if ask[i] > limit:
      temTotal += limit
    else:
      temTotal += ask[i]
  if temTotal <= total:
    return True
  else:
    return False

# execution
end = ask[-1]
start = 0
ans = 0
while end >= start:
  mid = (end + start) // 2
  if isCorrect(mid) == True:
    ans = mid
    start = mid+1
  else:
    end = mid - 1
print(ans)
