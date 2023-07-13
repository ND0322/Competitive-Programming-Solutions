from queue import Queue

import sys

sys.setrecursionlimit(10**6)

def prune(node):


  visited[node] = True
  
  if node != r[0]:

    
    if len(adj[node]) == 1:
      if pho[node] == True:
  
        
  
  
  
        return True
     
      return False


  check = False

  for child in adj[node]:
    
    if not visited[child]:


      
      if prune(child):
        check = True
        graph[node].append(child)
        graph[child].append(node)
       
        

  if check or pho[node]:
    return True
  return False
  




  
n,m = map(int,input().split(" "))


pho = [False] * (n)
visited = [False] * (n)
r= list(map(int,input().split(" ")))

for i in r:
  pho[i] = True




adj = []
graph = []

for i in range(n):
  adj.append([])
  graph.append([])

for i in range(n-1):
  x,y = map(int,input().split(" "))

  adj[x].append(y)
  adj[y].append(x)


  
prune(r[0])



sub = [False] * n

for i in range(len(graph)):
  if len(graph[i]) > 0:
    sub[i] = True

q = Queue()
visited = [False] * n
distances = [-1] * n

q.put(r[0])

visited[r[0]] = True
distances[r[0]] = 0

while not q.empty():
  node = q.get()

  for child in graph[node]:
    if not visited[child]:
      visited[child] = True
      distances[child] = distances[node] + 1
      q.put(child)


far = distances.index(max(distances))

q = Queue()
visited = [False] * n
distances = [-1] * n





q.put(far)

visited[far] = True
distances[far] = 0

while not q.empty():
  node = q.get()

  for child in graph[node]:
    if not visited[child]:
      visited[child] = True
      distances[child] = distances[node] + 1
      q.put(child)




end = distances.index(max(distances))



ans = 0

visited = [False] * n

def dfs(node):



  


  global ans
  
  if node == end:
    return True

  
  if len(graph[node]) == 1 and node != far:

    
    
    
    return False

  

  

  visited[node] = True


  check = False

  for child in graph[node]:
    
    if not visited[child]:

      if dfs(child):
        check = True
      else:
        ans += 1
        

  
  if check:
    return True
  return False
  
dfs(far)



print(max(distances) + 2*ans)
