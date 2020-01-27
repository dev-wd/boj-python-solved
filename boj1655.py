from heapq import heappush, heappop
import sys
input = sys.stdin.readline
minq = []
maxq = []

n = int(input())
ans = []
for i in range(n):
  tem = int(input())
  qtem = 0
  if tem >= 0:
    qtem = -tem
  else:
    qtem = -tem *0.0001

  if i == 0:
    heappush(maxq,(qtem,tem))
    ans.append(maxq[0][1])
    continue
  if i == 1:
    if maxq[0][1] > tem:
      heappush(minq,heappop(maxq)[1])
      heappush(maxq,(qtem,tem))
      ans.append(maxq[0][1])
    else:
      heappush(minq,tem)
      ans.append(maxq[0][1])
    continue
  
  if minq[0] > tem:
    heappush(maxq,(qtem,tem))
  else:
    heappush(minq,tem)
  
  while(1):
    if (len(maxq) == len(minq)+1) or (len(maxq) == len(minq)):
      break
    elif len(maxq) < len(minq):
      tem = heappop(minq)
      qtem = 0
      if tem >= 0:
        qtem = -tem
      else:
        qtem = -tem *0.0001
      heappush(maxq,(qtem,tem))
    else:
      heappush(minq,heappop(maxq)[1])
  ans.append(maxq[0][1])

for i in range(len(ans)):
  print(ans[i])
