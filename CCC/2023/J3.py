days = {}

n = int(input())

for i in range(n):
  day = input()
  for j in range(5):
    if day[j] == "Y":
      if j not in days:
        days[j] = 1
      else:
        days[j] += 1

ans = ""


days = dict(sorted(days.items(),key = lambda x:x[1], reverse = True))
target = days[list(days.keys())[0]]




for i in days:
  if days[i] == target:
    ans += str((i + 1)) + ','

ans = ans[0:len(ans) - 1]
print(ans)
