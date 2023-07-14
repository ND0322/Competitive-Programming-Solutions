def cycle(x):
  i = x
  while i != parents[i]:
    parents[i] = parents[parents[i]]
    i = parents[i]

  return i

def union(x,y):
  x = cycle(x)
  y = cycle(y)

  parents[x] = y

n = int(input())


buildings = [-1]

for i in range(n):
  buildings.append(tuple(map(int,input().split(" "))))



edges = []

for i in range(1,n):
  for j in range(i+1,n+1):
    d = abs(buildings[i][0] - buildings[j][0]) **2 + abs(buildings[i][1] - buildings[j][1]) **2
    edges.append((i,j,d))


parents = []

for i in range(n+1):
  parents.append(i)

edges.sort(key = lambda x:x[2])



w = int(input())



ans = 0
for i in range(w):
  x,y = map(int,input().split(" "))

  union(x,y)
mst = []
for node,child,weight in edges:
  if cycle(node) != cycle(child):
    mst.append((node,child,weight))
    ans += weight ** (1/2)
    union(node,child)
    
print("%.2f" % ans)
for i in mst:
  print(i[0],i[1])
