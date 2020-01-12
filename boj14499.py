import sys
import copy
input = sys.stdin.readline

# declare the input data
N, M, y, x, K = map(int,input().split())
mapList = []
for i in range(N):
  mapList.append(list(map(int,input().split())))
orderList = list(map(int,input().split()))

# turn the dice
diceDx = [0, 0, 0, 0]
diceDy = [0, 0, 0, 0]
def dice(dir, cx, cy):
  # east
  if dir == 1: 
    diceDx.insert(0,diceDx.pop())
    diceDy[3] = diceDx[3]
    diceDy[1] = diceDx[1]
  # west
  elif dir == 2:
    diceDx.append(diceDx.pop(0))
    diceDy[3] = diceDx[3]
    diceDy[1] = diceDx[1]
  # north
  elif dir == 3:
    diceDy.append(diceDy.pop(0))
    diceDx[3] = diceDy[3]
    diceDx[1] = diceDy[1]
  # south
  elif dir == 4:
    diceDy.insert(0, diceDy.pop())
    diceDx[3] = diceDy[3]
    diceDx[1] = diceDy[1]

  if mapList[cy][cx] == 0:
    mapList[cy][cx] = diceDx[3]
  else:
    diceDx[3] =  mapList[cy][cx]
    diceDy[3] =  mapList[cy][cx]
    mapList[cy][cx] = 0
  return diceDx[1]

# for each order direction
mapDx = [1, -1, 0, 0]
mapDy = [0, 0, -1, 1]
for i in range(len(orderList)):
  curDir = orderList[i]
  if  (x + mapDx[curDir-1] >= 0) and (x + mapDx[curDir-1] <= len(mapList[0]) - 1) and (y + mapDy[curDir-1] >= 0) and (y + mapDy[curDir-1] <= len(mapList) - 1):
    x += mapDx[curDir-1]
    y += mapDy[curDir-1]
    print(dice(curDir, copy.deepcopy(x), copy.deepcopy(y)))
