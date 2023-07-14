def solve():

  n,m = map(int,input().split(" "))
  
  
  adj = []
  
  for i in range(n+m+1):
    adj.append([])
  
  for i in range(int(input())):
    x,y = map(int,input().split(" "))
    adj[x].append(n+y)
    adj[n+y].append(x)
  
  
  for i in range(1,n+1):
  
    visited = [False] * (n+m+1)
  
    for j in adj[i]:
      for k in adj[j]:
        if i == k:
          continue
  
        if not visited[k]:
          visited[k] = True
  
        else:
          return "NO"
  return "YES"

print(solve())
