import math,sys



sys.setrecursionlimit(10**6)

def dfs(node,p):
  global time,ans
  
  visited[node] = True
  
  time += 1

  low[node] = time
  tin[node] = time

  for child in adj[node]:
    
    if child == p:
      continue
    if visited[child]:
      low[node] = min(low[node],low[child])
    else:
      dfs(child,node)
      low[node] = min(low[node],low[child])
      if low[child] > tin[node]:
        bridges.append((node,child))
        counter[node] += 1
        counter[child] += 1
        

      
  
  

n,m = map(int,input().split(" "))

edges = set()
adj = []

for i in range(n+1):
  adj.append([])



for i in range(m):
  x,y = map(int,input().split(" "))
  edges.add((x,y))
  edges.add((y,x))

  if i == 0:
    temp = (x,y)
  e = (x,y)


for x,y in edges:
  adj[x].append(y)

time = 0
tin = [-1] * (n+1)
low = [-1] * (n+1)
visited = [False] * (n+1)
counter = [0] * (n+1)
bridges = []

  
for node in range(1,n+1):
  if not visited[node]:
    dfs(node,-1)
    


if len(bridges) == 0:
  print(0)
else:
  cnt = 0
  for node,child in bridges:
    if counter[node] == 1 or counter[child] == 1:
      cnt += 1

  v = 0
  if max(counter) > 1:
    v = counter.count(max(counter))

  print((cnt+1-v//2)//2)
