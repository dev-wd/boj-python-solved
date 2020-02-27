import sys
input = sys.stdin.readline

# disjoint set & union-find
n, m = map(int,input().split()) 
parent = [i for i in range(n+1)]
def find(c):
  if(parent[c] == c): return c
  parent[c] = find(parent[c])
  return parent[c]

def union(ca,cb):
  rootOfca = find(ca)
  rootOfCb = find(cb)
  if not rootOfca == rootOfCb:
    parent[rootOfCb] = rootOfca

def check(ca,cb):
  if find(ca) == find(cb):
    return True
  else:
    return False

# finding answer
ans = []
for i in range(m):
  flag, a, b = map(int,input().split())
  if flag == 0 :
    union(a,b)
  else:
    if check(a,b):
      ans.append("YES")
    else:
      ans.append("NO")

for i in range(len(ans)):
  print(ans[i])
