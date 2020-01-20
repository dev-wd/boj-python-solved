import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
answer = []
for i in range(n):
  tc = list(map(int,input().split()))
  tq = deque(map(int,input().split()))
  final = []
  while(1):
    cv = tq.popleft()
    if len(tq) != 0 and cv < max(tq):
      tq.append(cv)
      if tc[1] == 0:
        tc[1] = len(tq)
      tc[1] -= 1
    else:
      if tc[1] == 0:
        answer.append(tc[0]-len(tq))
        break
      else:
        tc[1] -= 1
for i in range(len(answer)):
  print(answer[i])
