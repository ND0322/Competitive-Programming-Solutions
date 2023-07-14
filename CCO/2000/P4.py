from queue import Queue

n,w,p = map(int,input().split(" "))

adj = [-1]

for i in range(n):
  adj.append([])

for i in range(w):
  x,y,c = map(int,input().split(" "))
  adj[x].append((y,c))
  adj[y].append((x,c))


for i in range(p):
  start,end = map(int,input().split(" "))
  q = Queue()
  visited = [False for i in range(n+1)]
  distances = [-1] * (n + 1)

  q.put(start)
  visited[start] = True
  distances[start] = 0

  while not q.empty():
    node = q.get()

    for child in adj[node]:
      if visited[child[0]] == False:
        q.put(child[0])
        visited[child[0]] = True
        distances[child[0]] = distances[node] + child[1]

  print(distances[end])
