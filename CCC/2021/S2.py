row = int(input())
col = int(input())
decisions = {}

k = int(input())

for i in range(k):
  a = input()
  if a not in decisions.keys():
    decisions[a] = 0
  else:
    decisions.pop(a)

numR = 0
numC = 0
for key in decisions.keys():
  if key[0] == "R":
    numR += 1
  else:
    numC += 1

answer = numR * col + numC * row - (numR * numC * 2)

print(answer)
