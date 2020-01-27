from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
q = []
ans = []
for i in range(n):
  tem = int(input())
  if tem == 0:
    heappush(q,(-tem,tem))
    if not q: ans.append(0)
    else: 
      ans.append(heappop(q)[1])
  else:
    heappush(q,(-tem,tem))

for i in range(len(ans)):
  print(ans[i])
