from queue import Queue

wood = int(input())

tiles = []

m = int(input())
n = int(input())

visited = set()

floor = []

for i in range(m):
  floor.append(list(input()))


def bfs(si,sj):
  q = Queue()
  
  ans = 1
  
  q.put((si,sj))
  visited.add((si,sj))


  
  
  while not q.empty():
    
    node = q.get()
  
    
        
  
    if node[0] + 1 < m and (node[0] + 1,node[1]) not in visited:
      if floor[node[0] + 1][node[1]] == ".":
        visited.add((node[0] + 1,node[1]))
        q.put((node[0] + 1,node[1]))
        ans += 1
      
    if node[0] - 1 > -1 and (node[0] - 1,node[1]) not in visited:
      if floor[node[0] - 1][node[1]] == ".":
        visited.add((node[0] - 1,node[1]))
        q.put((node[0] - 1,node[1]))
        ans += 1
      
    if node[1] + 1 < n and (node[0],node[1] + 1) not in visited:
      if floor[node[0]][node[1] + 1] == ".":
        visited.add((node[0],node[1] + 1))
        q.put((node[0],node[1] + 1))
        ans += 1
      
    if node[1] - 1 > -1 and (node[0],node[1] -1) not in visited:
      if floor[node[0]][node[1] - 1] == ".":
        visited.add((node[0],node[1] -1 ))
        q.put((node[0],node[1] - 1))
        ans += 1

  return ans
    
    
for i in range(m):
  for j in range(n):
    if (i,j) not in visited and floor[i][j] == ".":
    
      
      tiles.append(bfs(i,j))
tiles.sort(reverse = True)

ans = 0
for i in tiles:
  if i > wood:
    break
  wood -= i
  ans += 1

if ans == 1:
  print(ans, "room,",wood,"square metre(s) left over")
else:
  print(ans, "rooms,",wood,"square metre(s) left over")
