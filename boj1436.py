import sys
input = sys.stdin.readline

n = int(input())

i = 0
time = 0
while(1):
  i+= 1
  curNum = str(i)
  search = '666'
  if search in curNum:
    time+=1
    if time == n:
      print(curNum)
      break
