import sys
input = sys.stdin.readline

target = input()
key = input()
count = 0
i = -1
while(i <= len(target)-len(key)-1):
  i += 1
  for j in range(len(key)-1):
    if key[j] == target[i+j]:
      if j == len(key) - 2:
        count += 1
        if i + len(key) - 1 <= len(target)-len(key)+1:
          i += len(key) - 2
    else:
      break
print(count)
