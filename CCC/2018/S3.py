#dont add steps when chained
#precompute conveyors

#nowadays i would have just iterated through [di+1,di-1] and so on
from queue import Queue

n, m = map(int, input().split(" "))

graph = []
exits = {}
ca = []
ctypes = "UDLR"
conveyors = {}


for i in range(n):
  graph.append(list(input()))
for i in range(len(graph)):
  for j in range(len(graph[i])):
    if graph[i][j] == "S":
      start = (i, j)

    if graph[i][j] == ".":

      exits[(i, j)] = -1
    if graph[i][j] in ctypes:
      ca.append((i,j))

for i in ca:
  visited = set()
  cur = i
  check = True

  while graph[cur[0]][cur[1]] in ctypes:
    
    
    if cur in visited:
      
      check = False
      break
    visited.add(cur)
    
    if graph[cur[0]][cur[1]] == "U":
      cur = (cur[0] - 1,cur[1])
    if graph[cur[0]][cur[1]] == "D":
      cur = (cur[0] + 1,cur[1])
    if graph[cur[0]][cur[1]] == "L":
      cur = (cur[0],cur[1] - 1)
    if graph[cur[0]][cur[1]] == "R":
      cur = (cur[0],cur[1] + 1)

  if check:
    conveyors[i] = cur


    
      
    
    


def cExecept(c):
  if c == "." or c == "U" or c == "D" or c == "L" or c == "R":
    return True
  return False


def checkCamera(i, j):
  if graph[i][j] == "C":
    return True
  if graph[i][j] == "." or graph[i][j] == "S":
    counter = 1

    while cExecept(graph[i - counter][j]):
      counter += 1
    if graph[i - counter][j] == "C":
      return True
    counter = 1

    while cExecept(graph[i + counter][j]):
      counter += 1
    if graph[i + counter][j] == "C":
      return True
    counter = 1

    while cExecept(graph[i][j - counter]):
      counter += 1
    if graph[i][j - counter] == "C":
      return True
    counter = 1

    while cExecept(graph[i][j + counter]):
      counter += 1
    if graph[i][j + counter] == "C":
      return True
    counter = 1
  return False


def isValid(x, y):
  
  if x >= 0 and x < n and y >= 0 and y < m and not checkCamera(
      x, y) and graph[x][y] != "W":
    
    
    if (x, y) not in visited:
      
      return True
  return False


q = Queue()


visited = set()

if isValid(start[0],start[1]):
  
  
  q.put((start))
  visited.add(start)
  distances = {(start):0}

  while not q.empty():
    node = q.get()
  
    #left
    
    if (node[0],node[1] -1) in conveyors:
      
      child = conveyors[(node[0],node[1] -1)]
    else:
      child = (node[0],node[1] -1)
  
    
    
  
   
    if isValid(child[0],child[1]):
      
      
      
      if graph[child[0]][child[1]] == ".":
        
        exits[(child[0], child[1])] = distances[node] + 1
  
        visited.add((child[0], child[1]))
        q.put((child[0], child[1]))
        distances[child] = distances[node] + 1
  
    #right
  
    if (node[0],node[1] + 1) in conveyors:
      
      child = conveyors[(node[0],node[1] + 1)]
    else:
      child = (node[0],node[1] + 1)
    if isValid(child[0],child[1]):
      if graph[child[0]][child[1]] == ".":
        exits[(child[0], child[1])] = distances[node] + 1
  
        visited.add((child[0], child[1]))
        q.put((child[0], child[1]))
        distances[child] = distances[node] + 1
  
    #up
    if (node[0] - 1,node[1]) in conveyors:
  
      
      
      
      child = conveyors[(node[0] - 1,node[1])]
      
    else:
      child = (node[0] - 1,node[1])
  
  
    if isValid(child[0],child[1]):
      
      if graph[child[0]][child[1]] == ".":
        exits[(child[0], child[1])] = distances[node] + 1
  
        visited.add((child[0], child[1]))
        q.put((child[0], child[1]))
        distances[child] = distances[node] + 1
    #down
        
    if (node[0] + 1,node[1]) in conveyors:
      
      child = conveyors[(node[0] + 1,node[1])]
    else:
      child = (node[0] + 1,node[1])
    if isValid(child[0],child[1]):
      if graph[child[0]][child[1]] == ".":
        exits[(child[0], child[1])] = distances[node] + 1
  
        visited.add((child[0], child[1]))
        q.put((child[0], child[1]))
        distances[child] = distances[node] + 1
  
  
for i in exits:
  print(exits[i])
