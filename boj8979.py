import sys
from operator import itemgetter
input = sys.stdin.readline

n, k = map(int, input().split())
c = []
for i in range(n):
  c.append(list(map(int,input().split())))

c.sort(key=itemgetter(3),reverse=True)
c.sort(key=itemgetter(2),reverse=True)
c.sort(key=itemgetter(1),reverse=True)

target = -1
for i in range(n):
  if c[i][0] == k:
    target = i

while(target != 0 and c[target][1:4] == c[target-1][1:4]): 
  target-=1 
print(target+1)
