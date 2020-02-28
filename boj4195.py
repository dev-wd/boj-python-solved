import sys
input = sys.stdin.readline

# union - find
def union(a,b):
  a = find(a)
  b = find(b)
  if not a == b:
    parent[b] = a 
    number[a] += number[b]

def find(c):
  if c == parent[c]:
    return c
  else:
    p = find(parent[c])
    parent[c] = p
    return parent[c]

# execusion
ans = []
n = int(input())
for i in range(n):
  f = int(input())
  parent = dict()
  number = dict() 
  for j in range(f):
    a, b = input().split()
    if not a in parent:
      parent[a] = a
      number[a] = 1
    if not b in parent:
      parent[b] = b
      number[b] = 1
    union(a,b)
    ans.append(number[find(a)]) 

for i in range(len(ans)):
  print(ans[i])
