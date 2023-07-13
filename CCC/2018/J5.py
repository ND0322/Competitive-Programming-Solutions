from queue import Queue

n = int(input())
graph = [[]]
for i in range(n):
  page = list(map(int,input().split(" ")))
  if page[0] == 0:
    graph.append([0])
  else:
    graph.append(page[1:page[0] + 1])


q = Queue()
visited = [False for i in range(n+1)]
output = []
distance = [0 for i in range(n+1)]
end = []

q.put(1)
visited[1] = True

while not q.empty():
  node = q.get()
  output.append(node)

  for child in graph[node]:
    if child == 0:
      end.append(distance[node] + 1)
    elif not visited[child]:
      visited[child] = True
      q.put(child)
      distance[child] = distance[node] + 1

if len(output) == n:
  print("Y")
else:
  print("N")

print(min(end))
