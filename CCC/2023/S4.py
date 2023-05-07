import heapq




n,m = map(int,input().split(" "))

edges = []

for i in range(m):
  x,y,l,c = map(int,input().split(" "))

  edges.append((l,c,x,y))

edges.sort()

parents = []

for i in range(n+1):
  parents.append(i)


mst = []


ans = 0
for i in range(n+1):
  mst.append([])
for edge in edges:
  l,c,node,child = edge

  

  pq = []
  distances = [float("inf")] * (n+1)

  heapq.heappush(pq,(0,node))
  distances[node] = 0

  

  while pq:
    d,no = heapq.heappop(pq)

    
    for nxt in mst[no]:
      
      ch = nxt[0]
      w = nxt[1]

     

      if distances[ch] > distances[no] + w:
        distances[ch] = distances[no] + w

        heapq.heappush(pq,(distances[ch],ch))

  d1 = distances[child]
  
 
  

  

  


  if l < d1:


    

    ans += c

    
    mst[node].append((child,l))
    mst[child].append((node,l))
    

print(ans)
    
