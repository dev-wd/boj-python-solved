import sys
from collections import deque
input = sys.stdin.readline

# group & lier List
n, m = map(int,input().split())
liers = deque(map(int,input().split()))
liers.popleft()
group = []
for i in range(m):
  group.append(list(map(int,input().split())))

# check for each groups
lierState = []
for i in range(m):
  lierState.append([])

ans = 0
alreadyLied = []
while(len(liers) != 0):
  curLier = liers.popleft()
  alreadyLied.append(curLier)
  for i in range(m):
    if curLier in group[i][1:]:
      lierState[i].append(True)
      for j in range(len(group[i])-1):
        curPerson = group[i][j+1]
        if (not curPerson in alreadyLied) and (not curPerson in liers):
          liers.append(curPerson)
    else:
      lierState[i].append(False)
         
for i in range(m):
  if True in lierState[i]:
    continue
  else:
    ans += 1

print(ans)
