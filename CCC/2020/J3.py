n = int(input())

x = []
y = []
for i in range(n):
  e = list(map(int,input().split(",")))
  x.append(e[0])
  y.append(e[1])
print(str(min(x) - 1) + "," + str(min(y) - 1))  
print(str(max(x) + 1) + "," + str(max(y) + 1))
