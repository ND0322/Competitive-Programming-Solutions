from queue import Queue

def dfs(node,parent):
  global ans
  
  dp[node][0] = 1
  for child in adj[node]:
    if child != parent:
      dfs(child,node)

      for i in range(1,diameter+1):


        ans += dp[child][i-1] * dp[node][diameter-i]
      for i in range(1,diameter+1):

        dp[node][i] += dp[child][i-1]
        
      
    
  
  


n = int(input())


adj = []

for i in range(n+1):
  adj.append([])
for i in range(n-1):
  x,y = map(int,input().split(" "))
  adj[x].append(y)
  adj[y].append(x)



q = Queue()
visited = [False] * (n+1)
distances = [0] * (n+1)

q.put(1)
visited[1] = True

while not q.empty():
  node = q.get()

  for child in adj[node]:
    if not visited[child]:
      visited[child] = True
      distances[child] = distances[node] + 1
      q.put(child)

u = distances.index(max(distances))



q.put(u)
visited = [False] * (n+1)
distances = [0] * (n+1)

visited[u] = True


while not q.empty():
  node = q.get()


  for child in adj[node]:
    if not visited[child]:
      visited[child] = True
      distances[child] = distances[node] + 1
      q.put(child)



diameter = max(distances)

ans = 0
dp = [[0] * (diameter+1) for i in range(n+1)]

dfs(1,0)

print(diameter+1,ans)
