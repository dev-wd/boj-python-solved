import sys
input = sys.stdin.readline
A, B, V = map(int,input().split())

daywork = A-B
target = V-A
if (int(target/daywork))*daywork+A >= V:
  print(int(target/daywork)+1)
else:
  print(int(target/daywork)+2)
