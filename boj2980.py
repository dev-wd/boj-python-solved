import sys
input = sys.stdin.readline

N, L = map(int, input().split())
TL = []
for i in range(N):
  TL.append(list(map(int, input().split())))
time = 0
distance = 0
while(TL):
  cD, cR, cG = TL.pop(0)
  time += cD - distance
  tem = time % (cR+cG)
  distance = cD
  if tem <= cR:
    time += cR - tem
time += L - distance
print(time)
