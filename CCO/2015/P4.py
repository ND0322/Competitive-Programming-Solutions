import sys

sys.setrecursionlimit(10**6)

#not done yet

def dfs(x,y):

  ans = []





  if not visited[x][y]:

    visited[x][y] = True
  
    if grid[x][y] == "W":
      for i in range(y-1,-1,-1):
        if grid[x][i].isalpha():
          ans.extend(dfs(x,i))
          ans.append((x,y))
          return ans
  
      return [(x,y)]

    if grid[x][y] == "E":
      for i in range(y+1,m):

        if grid[x][i].isalpha():
          ans.extend(dfs(x,i))
          ans.append((x,y))
          return ans
  
      return [(x,y)]

    if grid[x][y] == "N":
      for i in range(x-1,-1,-1):
   
        if grid[i][y].isalpha():
          ans.extend(dfs(i,y))
          ans.append((x,y))
          return ans
  
      return [(x,y)]

    if grid[x][y] == "S":
      for i in range(x+1,n):
        if grid[i][y].isalpha():
          ans.extend(dfs(i,y))
          ans.append((x,y))
          return ans
  
      return [(x,y)]

    

  else:
    return []
      

n,m = map(int,input().split(" "))

visited = [[False] * m for i in range(n)]

cars = []
grid = []

for i in range(n):
  row = list(input())
  grid.append(row)

  for j in range(m):
    if row[j].isalpha():
      cars.append((i,j))

ans = []
for i in cars:
  ans.extend(dfs(i[0],i[1]))

for i in ans:
  print("(" + str(i[0]) + "," + str(i[1]) + ")")
