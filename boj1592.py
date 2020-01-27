import sys
input = sys.stdin.readline
n, m ,l = map(int,input().split())

q = [0 for i in range(n)]
rotNum = 0
cur = 0
q[cur] = 1
while(1):
  rotNum+=1
  if q[cur] % 2 == 1: cur += l
  else: cur -= l
  if cur >= n: cur = cur % n
  if cur < 0: cur = cur + n
  q[cur] += 1
  if q[cur] == m:
    print(rotNum)
    break
