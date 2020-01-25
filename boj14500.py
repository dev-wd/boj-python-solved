import sys
input = sys.stdin.readline

N, M = map(int,input().split())
maplist = []
for i in range(N):
  maplist.append(list(map(int,input().split())))

dx = [[0,1,2,3],[0,1,0,1],[0,0,0,1],[0,0,1,1],[0,1,1,2]]
dy = [[0,0,0,0],[0,0,1,1],[0,1,2,2],[0,1,1,2],[0,0,1,0]]
convertedDx = [[0,-1,-2,-3],[0,-1,0,-1],[0,0,0,-1],[0,0,-1,-1],[0,-1,-1,-2]]
convertedDy = [[0,0,0,0],[0,0,-1,-1],[0,-1,-2,-2],[0,-1,-1,-2],[0,0,-1,0]]

rot = [[0,1],[0],[0,1,2,3,4,5,6,7],[0,1,4,5],[0,1,2,3]]


maxSum = 0
# cases of squares
for i in range(5):
  # iterate map
  for k in range(N):
    for l in range(M):
      # cases of rotation
      for j in range(len(rot[i])):
        curRot = rot[i][j]
        curDx = []
        curDy = []
        if curRot == 0:
          curDx = dx[i]
          curDy = dy[i]
        elif curRot == 1:
          curDx = convertedDy[i]
          curDy = dx[i]
        elif curRot == 2:
          curDx = convertedDx[i]
          curDy = convertedDy[i]
        elif curRot == 3:
          curDx = dy[i]
          curDy = convertedDx[i]
        elif curRot == 4:
          curDx = dx[i]
          curDy = convertedDy[i]
        elif curRot == 5:
          curDx = convertedDy[i]
          curDy = convertedDx[i]
        elif curRot == 6:
          curDx = convertedDx[i]
          curDy = dy[i]
        elif curRot == 7:
          curDx = dy[i]
          curDy = dx[i]
        
        if l+max(curDx) < M and k+max(curDy) < N and l+min(curDx) >=0 and k+min(curDy) >= 0:
          sumOfSquare = 0
          for p in range(4):
            sumOfSquare+=maplist[k+curDy[p]][l+curDx[p]]
          maxSum = max(sumOfSquare,maxSum)

print(maxSum)
