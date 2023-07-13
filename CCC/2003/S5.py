import heapq

n,m,d = map(int,input().split(" "))

adj = []

for i in range(n+1):
  adj.append([])


for i in range(m):
  x,y,c = map(int,input().split(" "))

  adj[x].append((y,c))
  adj[y].append((x,c))


key = [-float("inf")] * (n+1)
pq = []
b = [False] * (n+1)

key[1] = 0
heapq.heappush(pq,(0,1))

while pq:
  dist,node = heapq.heappop(pq)

  if b[node]:
    continue

  b[node] = True

  

  for c in adj[node]:
    child = c[0]
    weight = c[1]

    if (not b[child]) and key[child] < weight:
      key[child] = weight

      heapq.heappush(pq,(-key[child],child))


ans = float("inf")

for i in range(d):
  c = int(input())

  if key[c] < ans:
    ans = key[c]

print(ans)
