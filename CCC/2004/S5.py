while True:
  m,n = map(int,input().split(" "))

  if m == 0 and n == 0:
    break

  grid = []

  for i in range(m):
    grid.append(list(input()))

  dp = [[-1] * (n) for i in range(m)]

  if grid[m-1][0] == ".":
    dp[m-1][0] = 0
  else:
    dp[m-1][0] = int(grid[m-1][0])

  

  for i in range(m-2,-1,-1):
    if grid[i][0] == ".":
      dp[i][0] = dp[i+1][0]
    elif grid[i][0].isnumeric():
      dp[i][0] = dp[i+1][0] + int(grid[i][0])
    else:
      break

  
  for c in range(1,n):
    
    for d in range(m):
      if dp[d][c-1] >= 0:
        cur = dp[d][c-1]

        for i in range(d,m):
          if grid[i][c].isnumeric():
            
            cur += int(grid[i][c])

            if cur > dp[i][c]:
              dp[i][c] = cur
              
          elif grid[i][c] == ".":
            if cur > dp[i][c]:
              dp[i][c] = cur
          else:
            break

    for u in range(m-1,-1,-1):
      if dp[u][c-1] >= 0:
        cur = dp[u][c-1]

        for i in range(u,-1,-1):
          if grid[i][c].isnumeric():
            cur += int(grid[i][c])

            if cur > dp[i][c]:
              dp[i][c] = cur

          elif grid[i][c] == ".":
            if cur > dp[i][c]:
              dp[i][c] = cur
          else:
            break

  print(dp[m-1][n-1])
