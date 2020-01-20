import sys
input = sys.stdin.readline

n =  int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort(reverse=True)

S = 0
for i in range(len(A)):
  S+= A[i]*B[i]
print(S)
