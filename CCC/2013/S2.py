w = int(input())
t = []
n = int(input())
ans = 0
total=0
for i in range(n):
  t.append(int(input()))
for i in range (len(t)):
  if i>=4:
    total-=t[i-4]
  if (total+t[i])<=w:
    total+=t[i]
    ans+=1
  else:
    break




print(ans)
