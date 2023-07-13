from queue import Queue

t = int(input())

for test in range(t):
  r = int(input())
  c = int(input())

  grid = []

  for i in range(r):
    grid.append(list(input()))

  #bfs

  q = Queue()
  visited = set()
  distances = {(0,0):0}

  q.put((0,0))
  visited.add((0,0))

  while not q.empty():
    node = q.get()

    if grid[node[0]][node[1]] == "+" or grid[node[0]][node[1]] == "-":
      
      #right

      if node[1]+1<c and(node[0],node[1]+1) not in visited:
        
        if grid[node[0]][node[1]+1] != "*":
          
          q.put((node[0],node[1] + 1))
          distances[(node[0],node[1] + 1)] = distances[node] + 1
          visited.add((node[0],node[1] + 1))

      #left
      if node[1]-1>-1 and(node[0],node[1]-1) not in visited:
        if grid[node[0]][node[1]-1] != "*":
          q.put((node[0],node[1]-1))
          distances[(node[0],node[1]-1)] = distances[node] + 1
          visited.add((node[0],node[1]-1))
        
    if grid[node[0]][node[1]] == "+" or grid[node[0]][node[1]] == "|":
      #Up
      if node[0] - 1>-1 and(node[0] - 1,node[1]) not in visited:
        if grid[node[0] - 1][node[1]] != "*":
          q.put((node[0] - 1,node[1]))
          distances[(node[0] - 1,node[1])] = distances[node] + 1
          visited.add((node[0] - 1,node[1]))

      #Down
      if node[0]+1<r and(node[0]+1,node[1]) not in visited:
        if grid[node[0]+1][node[1]] != "*":
          q.put((node[0]+1,node[1]))
          distances[(node[0]+1,node[1])] = distances[node] + 1
          visited.add((node[0]+1,node[1]))

  
  if (r - 1, c-1) in distances:
    print(distances[(r - 1,c-1)] + 1)
  else:
    print(-1)
