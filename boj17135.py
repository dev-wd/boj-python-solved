import sys
import copy
from itertools import combinations

# matrix structure + input
input = sys.stdin.readline
N,M,D = map(int,input().split())
matrix = []
for i in range(N):
  matrix.append(list(map(int,input().split())))

caseIndexMatrix = list(combinations([i for i in range(M)],3))
for i in range(len(caseIndexMatrix)):
  caseIndexMatrix[i] = list(caseIndexMatrix[i])
# bfs
def bfs(cur_index):
  queue = [[N-1,cur_index,0]]
  while(queue):
  
    cur_yx = queue.pop(0)
    if temMatrix[cur_yx[0]][cur_yx[1]] == 1:
      return cur_yx
    
    # left
    if cur_yx[1] > 0 and cur_yx[2] < D-1:
      queue.append([cur_yx[0],cur_yx[1]-1,cur_yx[2]+1])
    # top
    if cur_yx[0] > 0 and cur_yx[2] < D-1:
      queue.append([cur_yx[0]-1,cur_yx[1],cur_yx[2]+1])
    # right
    if cur_yx[1] < M -1 and cur_yx[2] < D-1:
      queue.append([cur_yx[0],cur_yx[1]+1,cur_yx[2]+1])
    
  return 0

listans= []
# for all achure cases 
for i in range(len(caseIndexMatrix)):

  ans = 0
  temMatrix = copy.deepcopy(matrix)
  for j in range(N):
    check_dup = []
    tem1 = bfs(caseIndexMatrix[i][0])
    tem2 = bfs(caseIndexMatrix[i][1])
    tem3 = bfs(caseIndexMatrix[i][2])

    # remove duplicated case 
    if not tem1 == 0 :
      temMatrix[tem1[0]][tem1[1]] = 0
      check_dup.append(tem1[0:2])
    if not tem2 == 0 :
      temMatrix[tem2[0]][tem2[1]] = 0
      check_dup.append(tem2[0:2])
    if not tem3 == 0 :
      temMatrix[tem3[0]][tem3[1]] = 0
      check_dup.append(tem3[0:2])
    # How many achors dead 
    ans += len(set([tuple(set(check_dup)) for check_dup in check_dup]))
    temMatrix.pop()
    temMatrix.insert(0,[0 for k in range(M)])
  listans.append(ans)
print(max(listans)) 
# MAX die  = Answer
