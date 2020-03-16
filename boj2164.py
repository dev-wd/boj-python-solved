import sys
from collections import deque
input = sys.stdin.readline
n = int(input()) + 1
d = deque([ i for i in range(1,n)])
while len(d) != 1:
  d.popleft()
  d.append(d.popleft())
print(d[0])
