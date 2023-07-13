def solve(taken):
  if taken >= q:
    return (0,[])

  if t[taken] == -1:
    ans = (float("inf"),[])
  
    for nxt in range(taken+1,min(taken+m+1,q+1)):
  
      
      time = 0
      for i in people[taken:nxt]:
        if i[1] > time:
          time = i[1]
      r = solve(nxt - taken + taken) 
      res = time + r[0]
      
      if res < ans[0]:
        ans = (res,r[1])
        best = (taken,nxt)
    
  
        
  
        
    t[taken] = ans[0]
  return (t[taken],[])



m = int(input())

q = int(input())

people = []

t = [-1] * (q+1)
dp = [999999999] *(q+1)
g = [-1] * (q+1)

dp[q] = 0
g[q] = 0

for i in range(q):
  
  name = input()
  time = int(input())

  people.append((name,time))



    
for i in range(q,-1,-1):
  res = 0
  for j in range(i+1,min(i+m+1,q+1)):

    res = max(res,people[j-1][1])

    if dp[j] + res < dp[i]:
      dp[i] = dp[j] + res
      g[i] = j - i
      




print("Total Time:", dp[0])

p = [-1] * (q+1)
x = 0
y = (q)


while g[x] != 0:

  
  p[y] = g[x]
  
  y-=1

  x += g[x]

p = p[::-1]

start = 0
cnt = p[0]
index = 0

while p[index] != -1:
  pri = ""

  for i in people[start:cnt]:
    pri += i[0] + " "

  print(pri.strip())

  index += 1
  start = cnt
  cnt += p[index]
