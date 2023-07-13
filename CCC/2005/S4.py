t = int(input())

def dfs(node,depth):
  

  if len(graph[node]) == 0:
    return depth

  ans = depth
  for child in graph[node]:
    res = dfs(child,depth+1)
    if res > ans:
      ans = res
  return ans
    

for _ in range(t):
  n = int(input())

  l = []
  graph = {}

  for i in range(n):
    a = input()
    l.append(a)
    if a not in graph:
      graph[a] = []
    

  l = l[::-1]

  for i in range(n - 1):
    

    if l[i] not in graph[l[i+1]]:
      graph[l[i]].append(l[i+1])
  print(n * 10 - 2 * dfs(l[0],0) * 10)
