x = int(input())


xqueries = []
yqueries = []

for i in range(x):
  xqueries.append(tuple(map(str,input().split(" "))))

y = int(input())

for i in range(y):
  yqueries.append(tuple(map(str,input().split(" "))))

name = {}

n = int(input())

parents = [-1] * (n*3)

for i in range(n):
  x,y,z = map(str,input().split(" "))

  name[x] = i * 3 
  name[y] = i*3+1
  name[z] = i*3+2

  parents[name[x]] = i
  parents[name[y]] = i
  parents[name[z]] = i

ans = 0

for x,y in xqueries:
  if parents[name[x]] != parents[name[y]]:
    ans+=1
for x,y in yqueries:
  if parents[name[x]] == parents[name[y]]:
    ans+=1
print(ans)
