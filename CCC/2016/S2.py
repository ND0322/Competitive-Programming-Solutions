type = int(input())
n = int(input())

d = list(map(int, input().split(" ")))
p = list(map(int, input().split(" ")))
ans = 0

d.sort()
if type == 1:
  p.sort()
else:
  p.sort(reverse = True)

for i in range(n):
  ans += max(d[i],p[i])
print(ans)
