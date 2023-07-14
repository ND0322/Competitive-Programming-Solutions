def solve():
  n = int(input())
  
  addresses = [-1] * 101
  
  
  ntn = []
  adj = [-1] * n
  
  
  for i in range(n):
    p,s,t = map(str,input().split(" "))
  
    ntn.append(p)
  
    addresses[int(s)] = i
  
    adj[i] =int(t)
  
  

  def findCycle(root):
    slow = root
    fast = root

    while slow != -1 and fast != -1 and addresses[adj[fast]] != -1:
      slow = addresses[adj[slow]]
      fast = addresses[adj[addresses[adj[fast]]]]

      if slow == fast:
        return True

    return False


  for i in range(n):
    if findCycle(i):
      print("Impossible")
      return
  
  order = []



  def dfs(node):
    ans = []
  
  
    
  
  
  
    
    if addresses[adj[node]] == -1:
  
  
  
      if not visited[node]:
  
        visited[node] = True


        if ntn[node] not in order:
          return [ntn[node]]
        return []
      else:
        return []
  
  
    visited[node] = True
    if not visited[addresses[adj[node]]]:
  
      
  
      
      ans.extend(dfs(addresses[adj[node]]))

      if ntn[node] not in order:
        ans.extend([ntn[node]])
  
  
      
    return ans
  

  
  
  for i in range(n):
    visited = [False] * n
    order.extend(dfs(i))
  

  for i in order:
    print(i)




solve()
