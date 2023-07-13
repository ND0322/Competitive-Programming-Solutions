import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
  n = int(sys.stdin.readline())
  top = []
  branch = deque([])
  bottom = []
  index = 0

 
  for i in range(n):
    top.append(int(sys.stdin.readline()))
  top = top[::-1]
  check = True
  for cur in range(1,n+1):

    
    while index < len(top) and top[index] != cur and (len(branch) == 0 or branch[0] != cur):
      if len(branch) == 0:
        branch.appendleft(top[index])
        
        index += 1
        
      elif branch[0] > top[index]:
        branch.appendleft(top[index])
        index += 1
      else:
        check = False
        break

    if index < len(top):
      if top[index] == cur:
        bottom.append(top[index])
        index += 1
    if len(branch) > 0:
      if branch[0] == cur:
        bottom.append(branch[0])
        branch.popleft()
  
    if not check:
      break
      
  if len(bottom) == n:
    print("Y")
  else:
    print("N")
