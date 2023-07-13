from queue import Queue



n = int(input())
ans = []
adj = {}
for _ in range(n):
  site = input()
  if site not in adj:
    adj[site] = []

  while True:
    l = input()


    if l == "</HTML>":
      break
    l = l.split('"')

    for i in range(1,len(l) - 1,+2):
    
      adj[site].append(l[i])
      
    
      ans.append("Link from " + site + " to " + l[i])
     
      
    
    


while True:
    s = input()

    if s == "The End":
      break

    e = input()

    

    q = Queue()
    visited = set()

    q.put(s)
    visited.add(s)

    while not q.empty():
      node = q.get()

      if node in adj:
        
        
        for child in adj[node]:
          if child not in visited:
            q.put(child)
            visited.add(child)

    if e in visited:
      ans.append("Can surf from " + s + " to " + e + ".")
    else:
      ans.append("Can't surf from " + s + " to "+ e + ".")
for i in ans:
  print(i)
