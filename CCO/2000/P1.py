from queue import Queue

n = int(input())

sets = {}
todo = []

temp = []
for i in range(n):
  act = input().split(" contains ")

  temp.append([act[0],act[1]])
  if act[0] not in sets:
    sets[act[0]] = set()
    

  
  
  if act[1].isupper():
    todo.append(act)
    if act[1] not in sets:
      sets[act[1]] = set()
      
      
  
    
  sets[act[0]].add(act[1])



for t in todo:

  start = t[0]
  end = t[1]
  
  q = Queue()
  visited = set()
  
  q.put(end)
  visited.add(end)
  
  while not q.empty():
    node = q.get()


  
    if node.islower():
        
      sets[start].add(node)
    else:
      for child in sets[node]:
        if child not in visited:
          visited.add(child)
          q.put(child)


sets = dict(sorted(sets.items(),key = lambda x:x[0]))
ans = {}

for key in sets.keys():
  ans[key] = set()
  
for i in sets:
  for j in sets[i]:
    if j.islower():
      ans[i].add(j)



for i in ans:
  toP = i + " = {"
  s = sorted(ans[i])
  for j in s:
    
      toP += j +","

  if len(s) > 0:
    toP = toP[0:len(toP) - 1]
  toP += "}"
  print(toP)
