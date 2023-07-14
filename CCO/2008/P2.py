from queue import Queue

#todo

n,m = map(int,input().split(" "))

streets = {}

for i in range(n):
  x,y,type = map(str,input().split(" "))

  if x not in streets:
    streets[x] = []
    
  if y not in streets:
    streets[y] = []

  streets[x].append((y,type))
  streets[y].append((x,type))

for i in range(m):
  start,end = map(str,input().split(" "))
  if start not in streets or end not in streets:
    print("Unknown")
    continue
    

  q = Queue()
  relation = {}
  visited = {}
  
  for i in streets:
    relation[i] = -1
    visited[i] = False
    
  relation[start] = "parallel"
  q.put(start)
  check2 = True

  visited[start] = True

  while not q.empty():
    node = q.get()
    check = True

    
    if node == end:
      break
    for child,type in streets[node]:
      if not visited[child]:
        
        if type == "parallel" and relation[node] == "intersect":
          relation[child] = "intersect"
        elif type == "parallel" and relation[node] == "parallel":
          relation[child] = "parallel"
        elif type == "intersect" and relation[node] == "intersect":
          
          relation[child] = "parallel"
        elif type == "intersect" and relation[node] == "parallel":
          relation[child] = "intersect"

        q.put(child)
        visited[child] = True
          
      elif child == end:
        if type == "parallel" and relation[node] == "intersect":
          r = "intersect"
        elif type == "parallel" and relation[node] == "parallel":
          r = "parallel"
        elif type == "intersect" and relation[node] == "intersect":
          
          r = "parallel"
        elif type == "intersect" and relation[node] == "parallel":
          r = "intersect"

        if r != relation[node]:
              check = False
              print("Waterloo")
              break
    if not check:
      check2 = False
      break
    


  if check2:
    print(relation[end])
