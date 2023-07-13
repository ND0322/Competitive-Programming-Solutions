from queue import Queue

start = tuple(map(int,input().split(" ")))
end = tuple(map(int,input().split(" ")))


q = Queue()

visited = [[False] * 9 for i in range(9)]

distances = [[-1] * 9 for i in range(9)]

q.put(start)
visited[start[0]][start[1]]= True
distances[start[0]][start[1]] = 0


while not q.empty():
  node = q.get()
  
  if node == end:
    break
  
  children = []
  
  if node[0] + 2 < 9 and node[1] + 1 < 9:
    children.append((node[0]+2,node[1]+1))
    
  if node[0] + 2 < 9 and node[1] - 1 > 0:
    children.append((node[0]+2,node[1]-1))
    
  if node[0] - 2 > 0 and node[1] + 1 < 9:
    children.append((node[0]-2,node[1]+1))
    
  if node[0] - 2 > 0 and node[1] - 1 > 0:
    children.append((node[0]-2,node[1]-1))
    
  if node[0] + 1 < 9 and node[1] + 2 < 9:
    children.append((node[0]+1,node[1]+2))
    
  if node[0] + 1 < 9 and node[1] - 2 > 0:
    children.append((node[0]+1,node[1]-2))
    
  if node[0] - 1 > 0 and node[1] + 2 < 9:
    children.append((node[0]-1,node[1]+2))

  if node[0] - 1 > 0 and node[1] - 2 > 0:
    children.append((node[0]-1,node[1]-2))

  for cx,cy in children:
    if not visited[cx][cy]:
      visited[cx][cy] = True
      distances[cx][cy] = distances[node[0]][node[1]] + 1
      q.put((cx,cy))
      
print(distances[end[0]][end[1]])
