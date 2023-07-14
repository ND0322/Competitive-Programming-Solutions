def comp():
  def solve(type,cap):


    if type >= t:
      return 0
  
    if cap < 0:
      return -float("inf")


    if dp[type][cap] == -1:


      ans = 0
      for part in parts[type+1]:
  
        if cap - part[0] >= 0:
  
          ans = max(ans,solve(type+1,cap-part[0]) + part[1])
  
      dp[type][cap] = ans
    return dp[type][cap]
      


    

    

    
      
  
  t = int(input())
  
  parts = []

  dp = [[-1] * 3001 for i in range(6)]
  
  for i in range(t+1):
    parts.append([])
  
  for _ in range(int(input())):
    c,v,type = map(int,input().split(" "))
  
    parts[type].append((c,v))
  
  
  for i in range(1,len(parts)):
    if len(parts[i]) == 0:
      print(-1)
      return

  b = int(input())

  res = solve(0,b)

  if res == -float("inf"):
    print(-1)
  else:
    print(res)
  return


comp()
