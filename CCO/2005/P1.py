from queue import Queue


def solve():
  n,m = map(int,input().split(" "))
  
  grid = []
  for i in range(m):
    grid.append(list(map(int,input().split(" "))))

  
  for i in range(10):
    for j in range(i,10):
      for k in range(j,10):
        
        q = Queue()
        visited = [[False] * n for a in range(m)]
        nums = [i,j,k]


        for c in range(n):
          q.put((0,c))
          visited[0][c] = True
          

        while not q.empty():
          node = q.get()
            

            
          if node[0] == m-1:
            return str(i) + " " + str(j) + " " + str(k)

          if node[0] + 1 < m:
            if not visited[node[0]+1][node[1]] and grid[node[0]+1][node[1]] in nums:
              visited[node[0]+1][node[1]] = True
              q.put((node[0] + 1, node[1]))
  
          if node[0] - 1 > -1:
            if not visited[node[0]-1][node[1]] and grid[node[0]-1][node[1]] in nums:
              visited[node[0]-1][node[1]] = True
              q.put((node[0]-1, node[1]))
  
          if node[1] + 1 < n:
            if not visited[node[0]][node[1]+1] and grid[node[0]][node[1]+1] in nums:
              visited[node[0]][node[1]+1] = True
              q.put((node[0], node[1]+1))
  
          if node[1] - 1 > -1:
            if not visited[node[0]][node[1]-1] and grid[node[0]][node[1]-1] in nums:
              visited[node[0]][node[1]-1] = True
              q.put((node[0], node[1]-1))
  
  
  return "-1 -1 -1" 
  
  

print(solve())
