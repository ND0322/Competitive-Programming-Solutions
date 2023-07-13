n = int(input())
e = []
s = float("inf")
for i in range(n):
  e.append(int(input()))
e.sort()


for i in range(1,n - 1):

    s = min(s,(e[i] - e[i-1]) / 2 + (e[i+1] - e[i]) / 2)

   
print(s)
