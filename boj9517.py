import sys
input = sys.stdin.readline

currentPlayer = int(input())
numberOfQuestions = int(input())
questionCases = []
time = 0

for i in range(numberOfQuestions):
  a, b = map(str,input().split())
  a = int(a)
  questionCases.append([a,b])


for i in range(len(questionCases)):
  time += questionCases[i][0]
  if time >= 210:
    print(currentPlayer)
    break

  answer = questionCases[i][1]
  if answer == 'T':
    currentPlayer = (currentPlayer + 1) % 9
    if currentPlayer == 0:
      currentPlayer = 1
 
