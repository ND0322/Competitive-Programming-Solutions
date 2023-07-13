n = int(input())

f = int(input())
s = int(input())
t = int(input())

ans = 0
cur = 1
while n != 0:

  if cur == 1:
    f += 1
    if f == 35:
      n += 30
      f = 0
  if cur == 2:
    s += 1
    if s == 100:
      n += 60
      s = 0
  if cur == 3:
    t += 1
    if t == 10:
      n += 9
      t = 0

  n -= 1
  if cur == 3:
    cur = 1
  else:
    cur += 1
  ans += 1
    

print("Martha plays", ans, "times before going broke.")
