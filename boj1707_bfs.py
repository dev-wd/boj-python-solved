import sys
from collections import deque

input = sys.stdin.readline

# make the linkedList of graph
testCase = int(input())
totalTLinkedList = []
VEList = []
for i in range(testCase):
  V , E = map(int,input().split())
  tLinkedList = [ [] for j in range(V)]
  for k in range(E):
    tA, tB = map(int,input().split())
    tLinkedList[tA-1].append(tB-1)
  totalTLinkedList.append(tLinkedList)
  VEList.append([V,E])


# BFS
def BFS(indexV,tV,tE,curTCase):
  answer = True
  colorV = [ -1 for i in range(tV+1)]
  colorV[j] = 0
  # cur V, cur Color 
  queue = deque()
  queue.append(j)

  while(queue):
    curQ = queue.popleft()
    thisTime = totalTLinkedList[curTCase][curQ]
    for i in range(len(thisTime)):
      if colorV[thisTime[i]] == -1:
        queue.append(thisTime[i])
        colorV[thisTime[i]] = (colorV[curQ]+1)%2
      elif colorV[thisTime[i]] == colorV[curQ]:
        answer = False
        return answer
  return answer

# find answer
ansList = []
for i in range(len(totalTLinkedList)):
  tmVEList = VEList[i]
  for j in range(tmVEList[0]):
    if BFS(j,tmVEList[0],tmVEList[1],i) == False:
      ansList.append("NO")
      break
  if len(ansList) != i+1:
    ansList.append("YES")

# print answer
for i in range(len(ansList)):
  print(ansList[i])
