from queue import Queue
from math import lcm

while True:
  n = int(input())

  if n == 0:
    break

  adj = []

  for i in range(n+1):
    adj.append([])

  for i in range(n):
    x,y = map(int,input().split(" "))
    adj[x].append(y)

  times = []
  for start in range(1,n+1):
    q= Queue()

    distances = [0] * (n+1)

    q.put(start)

    cnt = 0
    while not q.empty():
      node = q.get()

      if node == start and distances[node] >0:
        break


      for child in adj[node]:
        q.put(child)
        distances[child] = distances[node] + 1

    times.append(distances[start])

  l = 1
  for i in times:
    l = lcm(l,i)

  print(l)
