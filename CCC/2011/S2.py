n = int(input())
sAns = []
rAns = []

ans = 0
for i in range(n):
  sAns += input()

for i in range(n):
  rAns += input()




for i in range(n):
  if sAns[i] == rAns[i]:
    ans += 1

print(ans)
