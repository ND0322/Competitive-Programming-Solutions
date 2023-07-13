import sys
import math


"""
sys.setrecursionlimit(10**6)



n = int(input())

dp = [float("inf")] * (n+1)

def factor(num):
    ans = [[1, num],[num,1]]
    
    for i in range (2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            ans.append([i,num//i])
            ans.append([num//i,i])
    return ans


def solve(num):
  if num == n:
    return 0
  if num > n:
    return float("inf")


  if dp[num] == float("inf"):
    
    small = float("inf")
    for i in factor(num):
      res = solve(num + i[0]) + i[1]
      
  
      if res < small:
        small = res
  
    dp[num] = small
  return dp[num]

dp[1] = 0

for i in range(1,n+1):
 

  for j in factor(i):
    if i + j[0] < n+1:

      
      dp[i+j[0]] = min(dp[i+j[0]],dp[i] + j[1])


print(dp)

print(dp[n])
"""

n = int(input())
ans = 0
while n > 1:
  for i in range(2,n+1):
    if n % i == 0:

      temp = n
      n -= n//i

      ans += (n // (temp//i))
      


      break

print(ans)
