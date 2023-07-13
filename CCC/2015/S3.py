import sys


def find(ele):
  if ele != dSet[ele]:
    dSet[ele] = find(dSet[ele])
  return dSet[ele]

def union(x,y):
  dSet[find(x)] = find(y)

g = int(sys.stdin.readline())
p = int(sys.stdin.readline())
cnt = 0
check = True
  
dSet = [0 for i in range(10**5 + 1)]

for i in range(1,g+1):
  dSet[i] = i

while cnt < p and check:
  gate = int(input())
  gateSet = find(gate)

  if gateSet == 0:
    print(cnt)
    check = False
  union(gateSet,gateSet - 1)
  cnt += 1
if check:
  print(p)
