n = int(input())
numGold = 0
for i in range(n):
  x = int(input())
  y = int(input())

  if ((x * 5) - (y * 3)) > 40:
    numGold+= 1

if (numGold == n):
  print(str(numGold) + "+")
else:
  print(numGold)
