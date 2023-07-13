from queue import Queue


while True:
  n = int(input())

  if n == 0:
    break

  s = input().split(" ")
  
  if n == 1:
    
    print(0)
    continue

  

  

  game = ""
  for i in s:
    game += i
    game += ","

  game = game[:len(game)-1]

  check = ""

  for i in range(1,n+1):
    check += str(i) + ","

  check = check[:len(check) - 1]

  q =Queue()

  visited = set()

  visited.add(game)

  q.put((game,0))

  b = True
  while not q.empty():
    node,d = q.get()




    l = node.split(",")


    if node == check:
      print(d)
      b = False
      break
        

    

    for i in range(n):
      if i - 1 > -1 and int(l[i][0]) != 0:

        

        if int(l[i-1][0]) > int(l[i][0]) or int(l[i-1][0] == "0"):

          

          child = ",".join(l[:i-1])

          

          if i-1 > 0:
            child += ","

          if l[i-1][0] == "0":
            child += l[i][0] + ","
          else:
            child += l[i][0] + l[i-1] + ","
          
          if len(l[i]) == 1:
            child += "0,"
            
          else:
            child += l[i][1:] + ","

          child += ",".join(l[i+1:])

          if child[-1] == ",":
            child = child[:len(child) - 1]

          if child not in visited:
            
            visited.add(child)
            q.put((child,d+1))
            
      if i + 1 < len(l) and int(l[i][0]) != 0:

        
        if int(l[i+1][0]) > int(l[i][0]) or l[i+1][0] == "0":

          

          

      
          child = ",".join(l[:i])

          if len(l[:i]) > 0:

            child += ","

          

          if len(l[i]) == 1:
            child += "0,"
            
          else:
            child += l[i][1:] + ","

          if l[i+1][0] == "0":
            child += l[i][0] + ","
          else:
            child += l[i][0] + l[i+1] + ","
          
          
          
          

          child += ",".join(l[i+2:])

          if child[-1] == ",":
            child = child[:len(child) - 1]

          if child not in visited:
            visited.add(child)
            q.put((child,d+1))

  if b:
    print("IMPOSSIBLE")
