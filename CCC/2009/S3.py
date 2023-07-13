from queue import Queue

adj = {1:{6},2:{6},3:{5,4,6,15},4:{3,6,5},5:{6,4,3},6:{1,2,3,4,5,7},7:{6,8},8:{9,7},9:{10,12,8},10:{11,9},11:{12,10},12:{9,11,13},13:{12,14,15}, 14:{13}, 15:{13,3},16:{18,17},17:{16,18},18:{17,16}}
while True:
  query = input()

  if query == "q":
    break
  if query == "i":
    x = int(input())
    y = int(input())

    if x not in adj:
      adj[x] = {y}
    else:
      adj[x].add(y)

    if y not in adj:
      adj[y] = {x}
    else:
      adj[y].add(x)
  if query == "d":
    x = int(input())
    y = int(input())

    adj[x].remove(y)
    adj[y].remove(x)
  if query == "n":
    n = int(input())
    print(len(adj[n]))
  if query == "f":

    n = int(input())
    temp = set()
    toR = []
    for i in adj[n]:
      toR.append(i)
      temp.update(adj[i])
      
    for i in toR:
      if i in temp:
        temp.remove(i)
    temp.remove(n)
   
    print(len(temp))
  if query == "s":
    n = int(input())
    target = int(input())
    
    q = Queue()
    visited = set()
    distances = {n:0}

    q.put(n)
    visited.add(n)
  
    while not q.empty():
      node = q.get()

      for friend in adj[node]:
        if friend not in visited:
          q.put(friend)
          visited.add(friend)
          distances[friend] = distances[node] + 1

    if target in distances:
      print(distances[target])
    else:
      print("Not connected")
