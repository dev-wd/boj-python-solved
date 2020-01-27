from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
q = []
ans = []
for i in range(n):
  tem = int(input())
  if tem == 0:
    #heappush(q,tem)
    if not q: ans.append(0)
    else: 
      ans.append(heappop(q))
  else:
    heappush(q,tem)

for i in range(len(ans)):
  print(ans[i])
