import heapq

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

inputs = []


edges = [[-1] * (1002) for i in range(1002)]



for i in range(n):
  inp = list(map(int,input().split(" ")))

  e = inp[0]

  corners = inp[1:e+1]
  costs= inp[e+1:]

  for j in range(e-1):
    
    if edges[corners[j]][corners[j+1]] == -1:
      edges[corners[j]][corners[j+1]] = [costs[j],i]
    else:
      if costs[j] < edges[corners[j]][corners[j+1]][0]:
        edges[corners[j]][corners[j+1]] = [costs[j],i]
      else:
        edges[corners[j]][corners[j+1]].append(i)

    if edges[corners[j+1]][corners[j]] == -1:
      edges[corners[j+1]][corners[j]] = [costs[j],i]
    else:
      if costs[j] < edges[corners[j+1]][corners[j]][0]:
        edges[corners[j+1]][corners[j]] = [costs[j],i]
      else:
        edges[corners[j+1]][corners[j]].append(i)

  if edges[corners[-1]][corners[0]] == -1:
      edges[corners[-1]][corners[0]] = [costs[-1],i]
  else:
    if costs[-1] < edges[corners[-1]][corners[0]][0]:
      edges[corners[-1]][corners[0]] = [costs[-1],i]
    else:
      edges[corners[-1]][corners[0]].append(i)

  if edges[corners[0]][corners[-1]] == -1:
      edges[corners[0]][corners[-1]] = [costs[-1],i]
  else:
    if costs[-1] < edges[corners[0]][corners[-1]][0]:
      edges[corners[0]][corners[-1]] = [costs[-1],i]
    else:
      edges[corners[0]][corners[-1]].append(i)





  
  
added = [[-1] * (1002) for i in range(1002)]


edg = []


for i in edges:
  for j in i:
    if j == -1:
      continue

    if len(j) == 2:
      if (added[j[1]][n] < 0 and added[n][j[1]] < 0) or j[0] < added[n][j[1]]:

        edg.append((j[1],n,j[0]))

        
        
        added[j[1]][n] = j[0]
        added[n][j[1]] = j[0]

    else:
      if (added[j[1]][j[2]] < 0 and added[j[2]][j[1]] < 0) or j[0] < added[j[1]][j[2]]:

        edg.append((j[1],j[2],j[0]))
        
        added[j[1]][j[2]] = j[0]
        added[j[2]][j[1]] = j[0]




edg.sort(key = lambda x:x[2])



parents = []
ans = 0

for i in range(n+1):
  parents.append(i)
  

for edge in edg:
  node = edge[0]
  child = edge[1]
  weight = edge[2]

  if node == n or child == n:
    continue

  if cycle(node) != cycle(child):
    ans += weight
    union(node,child)

check = True
for i in range(n-1):
  if cycle(i) != cycle(i+1):
    check = False
    
edg.sort(key = lambda x:x[2])

parents = []
ans2 = 0

mst = []

for i in range(n+1):
  parents.append(i)
  

for edge in edg:
  node = edge[0]
  child = edge[1]
  weight = edge[2]

 

  if cycle(node) != cycle(child):
    ans2 += weight
    union(node,child)
    mst.append((node,child,weight))


if check:
  print(min(ans,ans2))
else:
  print(ans2)
