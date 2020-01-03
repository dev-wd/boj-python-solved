import sys
import copy
input = sys.stdin.readline

# recursion
def rec(n):
  cur_n = copy.deepcopy(n)
  tem = numberCaseList[cur_n]
  if tem != -1:
    return tem
  else:
    total = 0
    total += (rec(cur_n-1) + rec(cur_n-2) + rec(cur_n-3))
    numberCaseList[cur_n] =  total 
    return total

# make inputList
testN = int(input())
inputList = []
for i in range(testN):
  inputList.append(int(input()))

# make numberCaseList 
numberCaseList = []
for i in range(11):
  numberCaseList.append(-1)
numberCaseList[0] = 1
numberCaseList[1] = 2
numberCaseList[2] = 4

rec(11 - 1)
for i in range(len(inputList)):
  print(numberCaseList[inputList[i]-1])
