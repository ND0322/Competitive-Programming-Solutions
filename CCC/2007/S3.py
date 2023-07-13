from queue import Queue

n = int(input())

adj = {}

for i in range(n):
  x,y = map(int,input().split(" "))

  adj[x] = y


while True:
  start, end = map(int,input().split(" "))

  if start == 0 and end == 0:
    break


  
  
  q = Queue()
  visited = set()
  distances = {}

  q.put(start)
  distances[start] = -1
  visited.add(start)

  
  while not q.empty():
    node = q.get()
    

    child = adj[node]
    if child not in visited:
        q.put(child)
        visited.add(child)
        distances[child] = distances[node] + 1

  if end in distances:
    print("Yes", distances[end])
  else:
    print("No")
