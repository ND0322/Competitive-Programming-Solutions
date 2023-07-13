"""
BST too slow

class node:
  def __init__(self,score):
    self.left = None
    self.right = None
    self.score = score
    self.rank = 0


class tree:
  def __init__(self):
    self.root = None
    
  def insert(self,score):
    if self.root == None:
      self.root = node(score)
      return 0
      
  
    
    n = self.root
    ans = 0
  
    while True:
      if score < n.score:
        #lower rank go left
  
        ans += n.rank+1
        if n.left != None:
          n = n.left
        else:
          n.left = node(score)
          return ans
  
      else:
        
        n.rank += 1
        print(n.rank)
  
        if n.right != None:
          n = n.right
        else:
          n.right = node(score)
          return ans
          
  def Inorder(self,root):
 
    if (root == None):
        return
    else:
        self.Inorder(root.left)
        print(root.score,root.rank)
        self.Inorder(root.right)
      
n = int(input())


t = tree()
ans = 0
for i in range(n):
  ans += t.insert(int(input())) + 1

print(round(ans/n,2))

"""

#i should redo this with ordered statistic tree

def merge(arr,temp,l,m,r):

  

  i = l
  j = m+1
  k = l

  ans = 0

  while i <= m and j <= r:
    
    if arr[i] <= arr[j]:
      temp[k] = arr[i]
      i += 1
      k += 1
    else:
      temp[k] = arr[j]
      j += 1
      k += 1
      ans += (m - i + 1)

  while i <= m:
    temp[k] = arr[i]
    i += 1
    k += 1

  while j <= r:
    temp[k] = arr[j]
    j += 1
    k += 1

  
  for i in range(l,r+1):
    arr[i] = temp[i]




  return ans
  
    
    
      
def mergeSort(arr,temp,l,r):

  ans = 0
  if l < r:
    m = ((l+r)//2)
    ans += mergeSort(arr,temp,l,m)
    ans += mergeSort(arr,temp,m+1,r)
    ans += merge(arr,temp,l,m,r)

  return ans
    



n = int(input())
arr = []
temp = [-1] * n

for i in range(n):
  arr.append(int(input()))
print(round((n + mergeSort(arr,temp,0,n-1))/n,2))
