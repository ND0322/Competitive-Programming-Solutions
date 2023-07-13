c = int(input())



first = list(map(int,input().split(" ")))
second = list(map(int,input().split(" ")))

ans = 0

for i in range(c):
  
  if first[i] == 1:
    numTouching = 0
    if i + 1 < c:
      if first[i + 1] == 1:
        numTouching += 1
    if second[i] == 1 and i % 2 == 0:
      numTouching += 1
    if i - 1 > - 1:
      if first[i - 1] == 1:
        numTouching += 1

    ans += 3 - numTouching

  if second[i] == 1:
    numTouching = 0
    if i + 1 < c:
      if second[i + 1] == 1:
        numTouching += 1
    if first[i] == 1 and i % 2 ==0:
      numTouching += 1
    if i - 1 > - 1:
      if second[i - 1] == 1:
        numTouching += 1

    ans += 3 - numTouching
print(ans)
