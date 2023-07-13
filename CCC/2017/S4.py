import sys


n,m,d = map(int,sys.stdin.readline().split(" "))

adj = []



def cycle(parent,x):
  i = x

  while i != parent[i]:
    parent[i] = parent[parent[i]]
    i = parent[i]

  return i
    

def union(x,y):
  x = cycle(parents,x)
  y = cycle(parents,y)

  parents[x] = y

def union2(x,y):
  x = cycle(parents2,x)
  y = cycle(parents2,y)

  parents2[x] = y

  

cur = []
for i in range(m):
  x,y,c = map(int,sys.stdin.readline().split(" "))

  
  adj.append((x,y,c,i))
  



adj = sorted(adj,key = lambda x:x[2])



parents = []


for i in range(n+1):
  parents.append(i)



ans = 0

largest = 0

for edge in adj:
  node,child,weight,order = edge

  if cycle(parents,node) != cycle(parents,child):
    

    if order >= n-1:
      ans += 1
    if weight > largest:
      largest = weight
    union(node,child)







if largest < d:
  
  
  
  parents2 = []
  for i in range(n+1):
    parents2.append(i)



 

  for edge in adj:
    node,child,weight,order = edge

    
   

    if cycle(parents2,node) != cycle(parents2,child):
      if weight<largest or(weight==largest and order < n-1):
        union2(node,child)

      
      elif weight <= d and order < n-1:
        
        ans -= 1
        break
  

print(ans)
