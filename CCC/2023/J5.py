def dfs(i,j,dirx,diry,perp,cur):

  if cur == target:
    return 1

  if len(cur) >= len(target):
    return 0

  ans = 0
  if i+dirx < r and i + dirx > -1 and j + diry < c and j+diry > -1:
    ans += dfs(i+dirx,j+diry,dirx,diry,perp,cur + grid[i+dirx][j+diry])
  if perp and len(cur) > 1:
    if not dirx:
      if i+1 < r:
        ans += dfs(i+1,j,1,0,0,cur + grid[i+1][j])
      if i-1 > -1:
        ans += dfs(i-1,j,-1,0,0,cur+grid[i-1][j])
    elif not diry:
      if j+1<c:
        ans += dfs(i,j+1,0,1,0,cur + grid[i][j+1])
      if j-1 > -1:
        ans += dfs(i,j-1,0,-1,0,cur+grid[i][j-1])
    else:
      if i+dirx < r and i + dirx > -1 and j - diry < c and j-diry > -1:
        ans += dfs(i+dirx,j-diry,dirx,-diry,0,cur+grid[i+dirx][j-diry])
      if i-dirx < r and i - dirx > -1 and j + diry < c and j+diry > -1:
        ans += dfs(i-dirx,j+diry,-dirx,diry,0,cur+grid[i-dirx][j+diry])
  return ans
      
      
      

target = input()

r = int(input())
c = int(input())

grid = []

for i in range(r):
  grid.append(input().split(" "))

ans = 0
for i in range(r):
  for j in range(c):
    if grid[i][j] == target[0]:
      ans += dfs(i,j,1,0,1,target[0])
      ans += dfs(i,j,-1,0,1,target[0])
      ans += dfs(i,j,0,1,1,target[0])
      ans += dfs(i,j,0,-1,1,target[0])
      ans += dfs(i,j,1,1,1,target[0])
      ans += dfs(i,j,-1,1,1,target[0])
      ans += dfs(i,j,1,-1,1,target[0])
      ans += dfs(i,j,-1,-1,1,target[0])

print(ans)
