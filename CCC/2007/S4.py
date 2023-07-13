n = int(input())
adj = [[] * 1 for i in range(n + 1)]

while True:
  x,y = map(int,input().split(" "))
  if x == 0 and y == 0:
    break
    
  adj[x].append(y)

dp = [0 for i in range(n + 1)]
dp[1] = 1


"""
def dfs(i):
  if i == 1:
    return 1
  if dp[i] == -1:
    res = 0
    for child in adj[i]:
      res += dfs(child)
    dp[n] = res
  return dp[n]
"""

for i in range(1,n):
  for j in range(len(adj[i])):
    dp[adj[i][j]] += dp[i]
print(dp[n])
