from queue import Queue

#you need max bipartite matching for dmoj only

#0 is the source
#1 is o- patient
#2 is o+ patient
#3 is a- patient
#4 is a+ patient
#5 is b- patient
#6 is b+ patient
#7 is ab- patient
#8 is ab+ patient
#9 is o- donor
#10 is o+ donor
#11 is a- donor
#12 is a+ donor
#13 is b- donor
#14 is b+ donor
#15 is ab- donor
#16 is ab+ donor
#17 is the sink



def bfs():
  for i in range(len(level)):
    level[i] = -1

  level[0] = 0

  q = Queue()
  q.put(0)

  while not q.empty():
    node = q.get()

    
    for child in range(18):
      if node != child and adj[node][child] > 0 and level[child] < 0:
        level[child] = level[node] + 1
        q.put(child)

  if level[17] < 0:
    return False
  return True
        
  

  
def dfs(node,flow):



  if node == 17:
    return flow

  for child in range(18):
    if adj[node][child] > 0 and level[child] == level[node]+1:
      cur = min(flow,adj[node][child])
      temp = dfs(child,cur)

      if temp > 0:

        adj[node][child] -= temp

        adj[child][node] += temp
        return temp

  return 0

 


def dinics():
  ans = 0
  while bfs():
    while True:
      flow = dfs(0,float("inf"))
      if not flow:
        break
      ans += flow
  return ans
adj = [[0] * 18 for i in range(18)]



donors = list(map(int,input().split(" ")))

for i in range(8):
  adj[0][i+1] = donors[i]

for i in range(9,17):
  adj[1][i] = float("inf")

for i in range(10,17,2):
  adj[2][i] = float("inf")

adj[3][11] = float("inf")
adj[3][12] = float("inf")
adj[3][15] = float("inf")
adj[3][16] = float("inf")

adj[4][12] = float("inf")
adj[4][16] = float("inf")

adj[5][13] = float("inf")
adj[5][14] = float("inf")
adj[5][15] = float("inf")
adj[5][16] = float("inf")

adj[6][14] = float("inf")
adj[6][16] = float("inf")

adj[7][15] = float("inf")
adj[7][16] = float("inf")

adj[8][16] = float("inf")


patients = list(map(int,input().split(" ")))
for i in range(8):
  adj[i+9][17] = patients[i]
  
level = [0] * 18

print(dinics())
