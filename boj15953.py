import sys
input = sys.stdin.readline

first = [500,300,300,200,200,200,50,50,50,50,30,30,30,30,30,10,10,10,10,10,10]

second = [512, 256, 256, 128,128,128,128,64,64,64,64,64,64,64,64,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32]

n = int(input())
total = []
for i in range(n):
  case = list(map(int,input().split()))
  price = 0
  if case[0] != 0 and case[0] < 22:
    price += first[case[0]-1]
  if case[1] != 0 and case[1] < 32:
    price += second[case[1]-1]
  total.append(price)

for i in range(len(total)):
  if total[i] == 0:
    print(0)
  else:
    print(total[i],"0000",sep="")
