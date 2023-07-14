from collections import deque

n,m = map(int,input().split(" "))

adj = []

for i in range(n+1):
  adj.append([])

for i in range(m):
  x,y,c = map(int,input().split(" "))

  adj[x].append((y,c))

pq = deque()
distances1 = [float("inf")] * (n+1)
distances2 = [float("inf")] * (n+1)

distances1[1] = 0


pq.append((0,1)) #first dist second dist node

while pq:
  d,node = pq.popleft()

  

  for child, weight in adj[node]:
    if distances1[child] > d + weight:
      
      distances2[child] = distances1[child]
      distances1[child] = d + weight

      pq.append((distances1[child],child))



    
    elif distances1[child] != d + weight and distances2[child] > d + weight:
        
        distances2[child] = d + weight

        pq.append((distances2[child],child))

    
    
if distances2[n] == float("inf"):
  print(-1)
else:
  print(distances2[n])
