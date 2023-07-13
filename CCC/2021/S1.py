n = int(input())

ans = 0

e = list(map(float,input().split(" ")))
s = list(map(float,input().split(" ")))

for i in range(n):
  ans += (e[i] + e[i+1]) * s[i] / 2
print(ans)
