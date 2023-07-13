from copy import deepcopy

#i should redo this question with tarjans

def dfs(node):
  
  if node == 1:
    return True

  visited[node] = True


  
  for child in range(len(temp[node])):
    if temp[node][child] and not visited[child]:
      if dfs(child):
        return True

  return False




adj = [[0] * 26 for i in range(26)]

edges = []
while True:
  edge = input()
  if edge == "**":
    break
  adj[ord(edge[0]) - 65][ord(edge[1]) - 65] = 1
  adj[ord(edge[1]) - 65][ord(edge[0]) - 65] = 1
  edges.append((edge[0],edge[1]))

ans = []


for s,d in edges:

  visited = [False] * 26

  temp = deepcopy(adj)
  temp[ord(s)-65][ord(d)-65] = 0
  temp[ord(d)-65][ord(s)-65] = 0

  if not dfs(0):
    ans.append((s,d))


for s,d in ans:
  print(s+d)

print("There are",len(ans),"disconnecting roads.")
