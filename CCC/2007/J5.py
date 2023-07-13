stops = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]

a = int(input())
b = int(input())

s = int(input())
for i in range(s):
  stops.append(int(input()))
stops.sort()

dp = [-1 for i in range(len(stops))]

def solve(n):
  
  if n == len(stops) - 1:
    
    return 1
  if n >= len(stops):
    return 0
    
  if dp[n] == -1:
    res = 0
    for i in range(1,len(stops) - n):
      if stops[n + i] > stops[n] + b:
        break
      if stops[n + i] < stops[n] + a:
        continue

      
      else:
        res += solve(n + i)
    dp[n] = res
  return dp[n]

print(solve(0))
