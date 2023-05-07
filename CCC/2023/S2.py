#dmoj with pypy or online grader both pass

n = int(input())

mountains = list(map(int,input().split(" ")))

dp = [[float("inf")] * n for i in range(n)]

for i in range(n):
  dp[i][i] = 0
  if i < n-1:  
    dp[i][i+1] = abs(mountains[i] - mountains[i+1])



for i in range(n-3,-1,-1):
  for j in range(i+2,n):
    dp[i][j] = dp[i+1][j-1] + abs(mountains[i]-mountains[j])

ans = [float("inf")] * n



for i in range(n):
  for j in range(n):
    ans[abs(j-i)] = min(ans[abs(j-i)],dp[i][j])

print(" ".join(list(map(str,ans))))
    
    
