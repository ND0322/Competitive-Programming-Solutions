from queue import Queue

def solve():
  n,m = map(int,input().split(" "))
  
  adj = [0]
  
  for i in range(n):
    adj.append([])
  
  for i in range(m):
    x,y = map(int,input().split(" "))
    adj[x].append(y)
  
  start,end = map(int,input().split(" "))
  taller = []
  shorter = []
  
  q = Queue()
  visited = [False for i in range(n+1)]
  
  q.put(start)
  visited[start] = True
  
  while not q.empty():
    node = q.get()
    if node == end:
      return "yes"
    taller.append(node)
  
    for child in adj[node]:
      if not visited[child]:
        visited[child] = True
        q.put(child)
  
  if end in taller:
    return "yes"
    
  q = Queue()
  visited = [False for i in range(n+1)]
  
  q.put(end)
  visited[end] = True
  
  while not q.empty():
    node = q.get()
    if node == start:
      return "no"
    shorter.append(node)
  
    for child in adj[node]:
      if not visited[child]:
        visited[child] = True
        q.put(child)
        
  if start in shorter:
    return "no"
  return "unknown"

print(solve())
