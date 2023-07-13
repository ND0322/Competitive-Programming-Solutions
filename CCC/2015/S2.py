j = int(input())
a = int(input())

ans = 0

arr = [-1 for i in range(j + 1)]


for i in range(1,j+1):
  

  jersey = input()


  if jersey == 'M':
    arr[i] = 2
  elif jersey == 'S':

    arr[i] = 1
  elif jersey == 'L':
    arr[i] = 3

  ans = 0
for i in range(a):
  c,n = map(str,input().split(" "))

  if c == "L":
    c= 3
  if c == "M":
    c = 2
  if c == "S":
    c=1

  
 
  if arr[int(n)] >= c:
    ans += 1
    arr[int(n)] = -1
print(ans)
