import sys
import operator as op
from functools import reduce

input = sys.stdin.readline
n = int(input())
def com(x,y):
  if x < 1 or y <0 or x < y:
    raise ValueError
  y = min(y, x-y)
  numerator = reduce(op.mul,range(x,x-y,-1),1)
  denominator = reduce(op.mul, range(1, y+1),1)
  return numerator // denominator

ans = 0
temn = n
t = 0
while(temn>=t):
  ans+=com(temn,t)
  t+=1
  temn-=1

print(int(ans)%10007)

