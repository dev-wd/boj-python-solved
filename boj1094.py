import sys
import copy
input = sys.stdin.readline

X = float(input())
branchList = [64.0]
if X == 64:
  print(1)
else:
  while(True):
    a = copy.deepcopy(branchList.pop())
    branchList.append(float(a/2))
    if not sum(branchList) >= X:
      branchList.append(float(a/2))
    if sum(branchList) == X:
      break
  print(len(branchList))
