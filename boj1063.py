import sys
input = sys.stdin.readline

# input
k, d, n = input().split()
n = int(n)
dirList = []
for i in range(n):
  dirList.append(input().rstrip('\n'))


# direction dictionary
raw = {"A": 0, "B": 1, "C": 2, "D": 3,  "E": 4, "F": 5,  "G": 6, "H": 7}
col = {"1": 7, "2": 6, "3": 5, "4": 4,  "5": 3, "6": 2,  "7": 1, "8": 0}
dx = {"R": 1, "L": -1, "B": 0, "T": 0,  "RT": 1, "LT": -1,  "RB": 1, "LB": -1}
dy = {"R": 0, "L": 0, "B": 1, "T": -1,  "RT": -1, "LT": -1,  "RB": 1, "LB": 1}


# iteration
curKX = raw[k[0]]
curKY = col[k[1]]
curDX = raw[d[0]]
curDY = col[d[1]]
for i in range(len(dirList)):
  nextKX = curKX + dx[dirList[i]]
  nextKY = curKY +  dy[dirList[i]]
  nextDX = curDX + dx[dirList[i]]
  nextDY = curDY +  dy[dirList[i]]
  
  if (curDX != nextKX or curDY != nextKY) and nextKX >= 0 and nextKX < 8 and nextKY >= 0 and nextKY < 8:
    curKX = nextKX
    curKY = nextKY
  if curDX == nextKX and curDY == nextKY and nextDX >= 0 and nextDX < 8 and nextDY >= 0 and nextDY < 8 and nextKX >= 0 and nextKX < 8 and nextKY >= 0 and nextKY < 8:
    curKX = nextKX
    curKY = nextKY
    curDX = nextDX
    curDY = nextDY

ansD = ""
ansK = ""
for key, value in raw.items():
  if curDX == value:
    ansD = key
  if curKX == value:
    ansK = key
for key, value in col.items():
  if curDY == value:
    ansD+=key
  if curKY == value:
    ansK+=key

print(ansK)
print(ansD)
