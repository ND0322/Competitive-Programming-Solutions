n = int(input())
e = {}
max = 0

for i in range(n):
  s = list(map(int,input().split(" ")))
  e[s[0]] = s[1]

myKeys = list(e.keys())
myKeys.sort()
e = {i: e[i] for i in myKeys}

for i in range(1,len(e)):
  if abs(e[myKeys[i]] - e[myKeys[i-1]]) / (myKeys[i] - myKeys[i-1]) > max:
    max = abs(e[myKeys[i]] - e[myKeys[i-1]]) / (myKeys[i] - myKeys[i-1])
print(max)
