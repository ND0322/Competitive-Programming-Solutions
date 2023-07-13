n = int(input())

e = input()
r = input()
ans = 0
for i in range(n):
  if e[i] == "C" and r[i] == "C":
    ans += 1
print(ans)
