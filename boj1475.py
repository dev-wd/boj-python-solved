import sys
input = sys.stdin.readline

n = input()
namount = [0 for i in range(10)]

for i in range(len(n)-1):
  namount[int(n[i])] += 1

print(int(max(namount[0],namount[1],namount[2],namount[3],namount[4],namount[5],namount[7],namount[8],(namount[6]+namount[9])/2+(namount[6]+namount[9])%2)))
