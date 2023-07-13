def cycle(x,type):
  i = x

  if type == "P":
    parents = p1
  else:
    parents = p2
  while i != parents[i]:
    parents[i] = parents[parents[i]]
    i = parents[i]
  return i

def union(x,y,type):

  x = cycle(x,type)
  y = cycle(y,type)
  

  if type == "P":
    p1[x] = y
  else:
    p2[x] = y

n,m,p,q = map(int,input().split(" "))

cntP = n
cntC = m

tot = 0
edges = []

for i in range(p):
  x,y,c = map(int,input().split(" "))

  edges.append(("F",x,y,c))
  tot += c * n

for i in range(q):
  x,y,c = map(int,input().split(" "))

  edges.append(("P",x,y,c))

  tot += c * m

p1 = []
p2 = []

for i in range(n+1):
  p1.append(i)

for i in range(m+1):
  p2.append(i)

edges.sort(key = lambda x: x[3])


ans = 0

for type,node,child,cost in edges:
  
  if cycle(node,type) != cycle(child,type):
    union(node,child,type)
    if type == "P":
      
      cntP -= 1
      ans += cost * cntC
      
    else:
  
      cntC -= 1
      ans += cost * cntP


print(tot-ans)
