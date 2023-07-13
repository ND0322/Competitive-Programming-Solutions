n = int(input())
ans = 0
for i in range(n):
  e = input()

  if e[0] == "P":
    ans += 1500
  elif e[0] == "M":
    ans += 6000
  elif e[0] == "S":
    ans += 15500
  elif e[0] == "C":
    ans += 40000
  elif e[0] == "T":
    ans += 75000
  elif e[0] == "H":
    ans += 125000
print(ans)
