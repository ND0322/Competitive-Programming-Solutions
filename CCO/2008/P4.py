from queue import Queue

def dfs(i,j):
  if grid[i][j] == 'W':
    child = (i,j-1)
  if grid[i][j] == 'E':
    child = (i,j+1)
  if grid[i][j] == 'N':
    child = (i-1,j)
  if grid[i][j] == "S":
    child = (i+1,j)

  

  if child in visited or vis[child[0]][child[1]]:
    if target in visited:
      vis[child[0]][child[1]] = True
      global ans 
      ans += 1
      return True
    return False

  visited.add(child)
  res = dfs(child[0],child[1])
  if res:
    vis[child[0]][child[1]] = True
    return res
  return res
    


    
  


n,m = map(int,input().split(" "))

vis = [[False] * m for i in range(n)]
ans = 0


grid = []

for i in range(n):
  grid.append(list(input()))

for i in range(n):
  for j in range(m):
    
    if vis[i][j]:
      continue

    
    visited = set()

    target = (i,j)

    dfs(i,j)
print(ans)


"""
       q = Queue()

    visited = [[False] * m for i in range(n)]

    v = set()

    q.put((i,j))

    

    
    while not q.empty():
      node = q.get()

      if grid[node[0]][node[1]] == 'W':
        child = (node[0],node[1]-1)
      if grid[node[0]][node[1]] == 'E':
        child = (node[0],node[1]+1)
      if grid[node[0]][node[1]] == 'N':
        child = (node[0]-1,node[1])
      if grid[node[0]][node[1]] == 'S':
        child = (node[0]+1,node[1])

      if not visited[child[0]][child[1]]:
        q.put(child)
        visited[child[0]][child[1]] = True
        v.add(child)
        
    if visited[i][j]:
      ans += 1

      for k in v:
        vis[k[0]][k[1]] = True
    
    

print(ans)

      
      



    
"""
