import sys
input = sys.stdin.readline

# input
inputList = list(map(int,input().split()))

B = inputList[1]
A = inputList[0]

# A -> B
resultCount = 1

done = False
while A != B:
    lastNumber = B % 10
    if lastNumber == 1:
        # (1) -> remove 1 
        B = B // 10
        resultCount+=1
    elif lastNumber == 3 or lastNumber == 5 or lastNumber == 7 or lastNumber == 9:
        # odd number (3,5,7,9) -> count : -1
        resultCount = -1
        break
    else:
        # even number (2, 4, 6, 8, 0)
        B = B // 2
        if B < A:
            resultCount = -1
            break
        resultCount+=1

# answer
print(resultCount)
