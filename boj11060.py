from collections import deque
import sys

# input
input = sys.stdin.readline

n = int(input())
inputList = list(map(int,input().split()))

# bfs 
visitedIndex = []
# (index:, count:)
queue = deque([(0, 0)])
 
done = False
while not done:
    if len(queue) == 0:
        print(-1)
        break
        
    n = queue.popleft()
    currentIndex = n[0]
     
    if currentIndex == len(inputList)-1:
        print(n[1])
        break
         
     
    if currentIndex not in visitedIndex:
        visitedIndex.append(currentIndex)
        maxStep = inputList[currentIndex]+1
        for i in range(1, maxStep):
            queue.append((currentIndex+i, n[1]+1))
