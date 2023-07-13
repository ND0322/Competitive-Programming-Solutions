r,c = map(int,input().split(" "))

grid = [ [0] * c for i in range(r)]



k = int(input())

for i in range(k):
  x,y = map(int,input().split(" "))

  grid[x - 1][y - 1] = 1

dp = [ [0] * c for i in range(r)]


def solve(i,j):
  if i < 0 or j < 0:
    return 0
  if grid[i][j] == 1:
    return 0
  if i == 0 and j == 0:
    return 1

  if not dp[i][j]:
    dp[i][j] = solve(i - 1,j) + solve(i,j-1)
  return dp[i][j]

print(solve(r - 1, c -1))
